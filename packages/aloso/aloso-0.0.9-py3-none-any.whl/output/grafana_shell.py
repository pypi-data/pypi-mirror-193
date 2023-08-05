import logging
from fabric import Connection, Config
import config
from domain.grafana import Grafana


# Using SSH key
# KEY_FILE = '/exnovo/etc/ssh/'
# 'key_filename': KEY_FILE

# Using password
# 'connect_kwargs': {'password': config.ftp_password}


class GrafanaShell(Grafana):
    @staticmethod
    def connection():
        configuration = Config(overrides={'user': config.grafana_username,
                                          'port': config.grafana_port,
                                          'sudo': {'password': config.grafana_password}})
        try:
            conn = Connection(host=config.grafana_host, config=configuration)
            return conn
        except Exception as e:
            logging.error(f"Erreur de connexion au serveur : {e}")

    @staticmethod
    def install_grafana():
        conn = GrafanaShell.connection()

        grafana_deb_file = config.grafana_wget_url.split("/")[-1]

        commands = [
            'apt-get install -y adduser libfontconfig1',
            f'wget {config.grafana_wget_url}',
            f'dpkg -i {grafana_deb_file}',
            f'rm {grafana_deb_file}',
            'mv grafana.ini /etc/grafana/grafana.ini',
            'systemctl daemon-reload',
            'systemctl restart grafana-server'
        ]

        conn.put(config.grafana_ini_file)
        logging.info("Fichier de configuration de Grafana envoyé")

        try:
            for command in commands:
                if config.use_sudo:
                    conn.sudo(command)
                else:
                    conn.run(command)
            logging.info("Grafana installé avec succès")
        except Exception as e:
            logging.error(f"Erreur d'installaton de Grafana : {e}")

    @staticmethod
    def install_loki():
        conn = GrafanaShell.connection()

        loki_zip_file = config.loki_wget_url.split("/")[-1]

        conn.put(config.loki_yaml_file)
        conn.put(config.loki_service_file)

        commands = [
            f"wget {config.loki_wget_url}",
            f"unzip {loki_zip_file}",
            f"rm {loki_zip_file}",
            "mv loki-linux-amd64 /usr/local/bin/loki",
            "mkdir -p /data/loki",
            "mv loki-local-config.yaml /etc/loki-local-config.yaml",
            "mv loki.service /etc/systemd/system/loki.service",
            "systemctl daemon-reload",
            "systemctl start loki.service"
        ]
        try:
            for command in commands:
                if config.use_sudo:
                    conn.sudo(command)
                else:
                    conn.run(command)
            logging.info("Loki installé avec succès")
        except Exception as e:
            logging.error(f"Erreur d'installaton de Loki : {e}")

    @staticmethod
    def install_promtail():
        conn = GrafanaShell.connection()

        promtail_zip_file = config.promtail_wget_url.split("/")[-1]

        conn.put(config.promtail_yaml_file)
        conn.put(config.promtail_service_file)

        commands = [
            f"wget {config.promtail_wget_url}",
            f"unzip {promtail_zip_file}",
            f"rm {promtail_zip_file}",
            "mv promtail-linux-amd64 /usr/local/bin/promtail",
            "mv promtail-local-config.yaml /etc/promtail-local-config.yaml",
            "mv promtail.service /etc/systemd/system/promtail.service",
            "systemctl daemon-reload",
            "systemctl start promtail.service"
        ]
        try:
            for command in commands:
                if config.use_sudo:
                    conn.sudo(command)
                else:
                    conn.run(command)
            logging.info("Promtail installé avec succès")
        except Exception as e:
            logging.error(f"Erreur d'installaton de Promtail : {e}")

    @staticmethod
    def remove_grafana():
        conn = GrafanaShell.connection()
        commands = [
            'systemctl stop grafana-server',
            'dpkg -P grafana-enterprise',
            'rm -r /etc/grafana',
            'systemctl daemon-reload',
        ]
        for command in commands:
            if config.use_sudo:
                conn.sudo(command)
            else:
                conn.run(command)


if __name__ == "__main__":
    # GrafanaShell.install_grafana()
    # GrafanaShell.remove_grafana()
    GrafanaShell.install_loki()
    # GrafanaShell.install_promtail()
