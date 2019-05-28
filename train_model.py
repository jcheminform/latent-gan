import argparse
from runners.TrainModelRunner import TrainModelRunner


def train_model():
    parser = argparse.ArgumentParser(description="Load and train a model")

    parser.add_argument("--input-data-path", "-i", help="The path to a data file.", type=str, required=True)
    parser.add_argument("--output-model-folder", "-o", help="Prefix to the folder to save output model.", type=str)
    parser.add_argument("--decode-mols-save-path", "-dp", help="Path to save the decoded smiles", type=str)
    parser.add_argument("--n-epochs", type=int, help="number of epochs of training")
    parser.add_argument("--starting-epoch", type=int, help="the epoch to start training from")
    parser.add_argument("--batch-size", type=int, help="size of the batches")
    parser.add_argument("--lr", type=float, help="adam: learning rate")
    parser.add_argument("--b1", type=float, help="adam: decay of first order momentum of gradient")
    parser.add_argument("--b2", type=float, help="adam: decay of first order momentum of gradient")
    parser.add_argument("--n-cpu", type=int, help="number of cpu threads to use during batch generation")
    parser.add_argument("--latent-dim", type=int, help="dimensionality of the latent space")
    parser.add_argument("--img-size", type=int, help="size of each image dimension")
    parser.add_argument("--channels", type=int, help="number of image channels")
    parser.add_argument("--n-critic", type=int, help="number of training steps for discriminator per iter")
    parser.add_argument("--clip-value", type=float, help="lower and upper clip value for disc. weights")
    parser.add_argument("--sample-interval", type=int, help="interval between samples")
    parser.add_argument("--save-interval", type=int, help="interval between saving the model")
    parser.add_argument("--sample-after-training", type=int, help="Number of molecules to sample after training")
    parser.add_argument("--message", "-m", type=str, help="Number of molecules to sample after training")

    args = {k: v for k, v in vars(parser.parse_args()).items() if v is not None}

    runner = TrainModelRunner(**args)
    runner.run()


if __name__ == "__main__":
    train_model()