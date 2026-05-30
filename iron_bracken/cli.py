import sys
from .config import load_config
from .rhizome import RhizomeNode

def main():
    if len(sys.argv) < 3:
        print("bracken [config] [command]")
        sys.exit(1)
    config = load_config(sys.argv[1])
    node = RhizomeNode()
    if sys.argv[2] == "gossip":
        node.gossip("hello")
