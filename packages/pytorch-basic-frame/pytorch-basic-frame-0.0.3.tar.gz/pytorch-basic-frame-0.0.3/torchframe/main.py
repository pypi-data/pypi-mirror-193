from typing import *
from tqdm import tqdm
import torch
from torch.utils.data import random_split, Dataset, DataLoader
import torchmetrics
from tensorboardX import SummaryWriter
from .parse_args import parse_args
from .mean_loss import MeanLoss


class Frame:
    def __init__(self) -> None:
        self.parse(parse_args())
        self.init_paras()

    def check_device(self, gpus):
        if len(gpus):
            return "cuda"
        return "cpu"

    def parse(self, args):
        # dataset
        self.ROOT = args.root
        self.CLASSES = args.classes
        self.SPLIT_RATE = args.split_rate
        # train
        self.CKPT = args.ckpt
        self.DEVICE = self.check_device(args.gpus)
        self.EPOCHS = args.epochs
        self.BATCH_SIZE = args.batch_size
        self.LR = args.lr
        # save
        self.SAVE_NAME = args.save_name
        self.SAVE_SUFFIX = args.save_suffix

    def init_paras(self):
        # parameters
        self.START_EPOCH = 0
        self.BEST_ACC = 0
        # variables
        self.dataset: Dataset = None
        self.model: torch.nn.Module = None

    def prepare_data(self):
        if hasattr(self.dataset, "classes"):
            self.CLASSES = self.dataset.classes
        assert self.CLASSES
        self.train_dataset, self.val_dataset = random_split(
            self.dataset, self.SPLIT_RATE
        )
        self.train_dataloader = DataLoader(
            dataset=self.train_dataset, batch_size=self.BATCH_SIZE, shuffle=True
        )
        self.val_dataloader = DataLoader(
            dataset=self.val_dataset, batch_size=self.BATCH_SIZE, shuffle=False
        )

    def prepare_model(self):
        self.loss_fun = torch.nn.CrossEntropyLoss()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=self.LR)
        if self.CKPT:
            checkpoint = torch.load(self.CKPT)
            self.model.load_state_dict(checkpoint["model_state_dict"])
            self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
            self.START_EPOCH = checkpoint["epoch"]

        # if args.device:
        #     model = torch.nn.DataParallel(model,device_ids=args.device)
        self.model.to(self.DEVICE)

    def prepare_train_metric(self):
        self.train_accuracy = torchmetrics.Accuracy(
            task="multiclass", num_classes=len(self.CLASSES)
        )
        self.valid_accuracy = torchmetrics.Accuracy(
            task="multiclass", num_classes=len(self.CLASSES)
        )
        self.train_loss = MeanLoss(self.loss_fun)
        self.valid_loss = MeanLoss(self.loss_fun)
        self.writer = SummaryWriter("logs/{}".format(self.SAVE_NAME))

    def train(self):
        assert self.dataset, self.model
        self.prepare_data()
        self.prepare_model()
        self.prepare_train_metric()
        for epoch in range(self.EPOCHS):
            if epoch < self.START_EPOCH:
                continue
            self.run_single_epoch(epoch, train=True)
            self.run_single_epoch(epoch, train=False)
            self.record_epoch(epoch)

    def run_single_epoch(self, epoch, train=True):
        self.model.train() if train else self.model.eval()
        bar = tqdm(self.train_dataloader if train else self.val_dataloader)
        for batch, (x, y) in enumerate(bar):
            self.optimizer.zero_grad()
            x = x.to(self.DEVICE)
            y = y.to(self.DEVICE)
            output = self.model(x)
            loss_mode = self.train_loss if train else self.valid_loss
            loss_val = loss_mode(output, y)
            self.optimizer.step()
            # batch metric
            self.train_loss
            y_predict = torch.max(output, dim=1).indices
            accuracy = self.train_accuracy if train else self.valid_accuracy
            acc = accuracy(y_predict, y)
            bar.desc = "mode:{},epoch:{}/{},batch:{}/{},loss:{:.3f},acc{:.3f}".format(
                "train" if train else "valid",
                epoch + 1,
                self.EPOCHS,
                batch + 1,
                len(bar),
                loss_val,
                acc,
            )

    def record_epoch(self, epoch):
        self.epoch_train_acc = self.train_accuracy.compute()
        self.epoch_valid_acc = self.valid_accuracy.compute()
        self.epoch_train_los = self.train_loss.compute()
        self.epoch_valid_los = self.valid_loss.compute()
        self.writer.add_scalar("train_acc", self.epoch_train_acc, epoch)
        self.writer.add_scalar("valid_acc", self.epoch_valid_acc, epoch)
        self.writer.add_scalar("train_loss", self.epoch_train_los)
        self.writer.add_scalar("valid_loss", self.epoch_valid_los)
        self.save(epoch)

    def save_ckpt(self, epoch, path):
        torch.save(
            {
                "model_state_dict": self.model.state_dict(),
                "optimizer_state_dict": self.optimizer.state_dict(),
                "epoch": epoch,
            },
            path,
        )

    def save(self, epoch):
        self.save_ckpt(
            epoch, "weights/{}_ckpt_last.{}".format(self.SAVE_NAME, self.SAVE_SUFFIX)
        )
        if self.epoch_train_acc > self.BEST_ACC:
            self.BEST_ACC = self.epoch_train_acc
            self.save_ckpt(
                epoch,
                "weights/{}_ckpt_best.{}".format(self.SAVE_NAME, self.SAVE_SUFFIX),
            )
