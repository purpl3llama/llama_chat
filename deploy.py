import shutil
from os import path
from dotenv import dotenv_values

config = dotenv_values(".env")
tinkr_path = config['TINKR_DIRECTORY']
scripts_path = path.join(tinkr_path, "scripts")
lua_file_name = "ai_chat.lua"

def main():
    shutil.copyfile(path.join(".", lua_file_name), path.join(scripts_path, lua_file_name))

if __name__ == "__main__":
    main()