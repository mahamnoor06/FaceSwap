#!/bin/sh
!wget -P ./arcface_model https://github.com/neuralchen/SimSwap/releases/download/1.0/arcface_checkpoint.tar
!wget https://github.com/neuralchen/SimSwap/releases/download/1.0/checkpoints.zip
!unzip ./checkpoints.zip  -d ./checkpoints
!wget -P ./parsing_model/checkpoint https://github.com/neuralchen/SimSwap/releases/download/1.0/79999_iter.pth