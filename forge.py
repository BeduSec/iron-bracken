import yaml
import sys
from iron_bracken.config import load_config
from iron_bracken.payloads.hybrid import compile_payload

def main():
    if len(sys.argv) != 2:
        print("Usage: forge.py <operator.yml>")
        sys.exit(1)
    config_path = sys.argv[1]
    config = load_config(config_path)
    payload = compile_payload(config)
    payload.write("implant.bin")
    print("Payload forged: implant.bin")

if __name__ == "__main__":
    main()
