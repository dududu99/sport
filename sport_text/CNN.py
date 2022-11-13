import torch
import torch.nn.functional as F
from torch import nn


class TextCNN(nn.Module):

    def __init__(self):
        super(TextCNN, self).__init__()
        num_embeddings = 5844 + 1
        num_classes = 10

        embedding_dim = 300  # 300
        num_kernel = 100  # 100
        kernel_sizes = [3, 4, 5]  # 3,4,5
        dropout = 0.5  # 0.5

        self.embedding = nn.Embedding(num_embeddings, embedding_dim, padding_idx=0)
        self.convs = nn.ModuleList([nn.Conv2d(1, num_kernel, (k, embedding_dim)) for k in kernel_sizes])
        self.fc = nn.Sequential(
            nn.Linear(num_kernel * len(kernel_sizes), num_classes, bias=True),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        x = self.embedding(x)
        x = x.unsqueeze(1)
        x = [conv(x).squeeze(3) for conv in self.convs]
        x = [F.max_pool1d(e, e.size(2)).squeeze(2) for e in x]
        x = torch.cat(x, 1)
        x = self.fc(x)
        return x
