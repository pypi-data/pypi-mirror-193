from domain.frontend import Frontend
import logging
from fabric import Connection, Config
from patchwork.files import exists
import config


class FrontendShell(Frontend):

    @staticmethod
    def connection():
        configuration = Config(overrides={'user': config.frontend_username,
                                          'port': config.frontend_port,
                                          'sudo': {'password': config.frontend_password}})
        try:
            conn = Connection(host=config.frontend_host, config=configuration)
            return conn
        except Exception as e:
            logging.error(f"Erreur de connexion au serveur : {e}")

    @staticmethod
    def install():
        conn = FrontendShell.connection()

        if not exists(conn, ".nvm/versions/node/*"):
            conn.run(f"wget -qO- {config.nvm_wget_url} | bash")
            conn.run("source ~/.bashrc")
            conn.run("nvm install --lts")
            logging.info("Installation de nvm et nodejs")

        conn.run(f"unzip {config.frontend_zip_file} -d {config.frontend_project_dir}")
        conn.run(f"rm {config.frontend_zip_file}")
        conn.run(f"cd {config.frontend_project_dir}/src && npm install")
        conn.run(f"cd {config.frontend_project_dir}/src && npm run dev")
        logging.info("Projet installé et lancé")
