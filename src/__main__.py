import app
import os

def main():
    app.start()

if __name__ == "__main__":
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    work_dir = os.path.normpath(cur_dir + "/../")
    work_dir = work_dir.replace(os.sep, '/')
    os.environ["WORKSPACE"] = work_dir
    main()