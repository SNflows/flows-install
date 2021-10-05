import os, configparser

def main():

    configfile = f"{os.path.dirname(os.path.abspath(__file__))}/config.ini"

    config = configparser.ConfigParser()
    config.read(configfile)

    for section in config:

        if not len(config[section]):
            continue

        print(f"[{section}]")

        for key in config[section]:

            value = input(f"{key}[{config[section][key]}] = ")
            config[section][key] = value if value else config[section][key]

    with open(configfile, 'w') as fd:
        config.write(fd)

if __name__ == "__main__":
    main()
