import sys

from treasure_map.app import app

# launch
if __name__ == "__main__":
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
