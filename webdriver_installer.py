import logging
import logger_config
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import os

def main():
    logger = logger_config.setup_logger(log_level=logging.INFO, file_prefix="webdriver_installer")

    target_dir = r'C:\Automacoes\driver'

    try:
        chromedriver = ChromeDriverManager().install()
        logging.info(f'ChromeDriver instalado em: {chromedriver}')

        shutil.move(chromedriver, os.path.join(target_dir, 'chromedriver.exe'))
        logging.info(f'ChromeDriver movido para o diretório: {target_dir}')
    except Exception as e:
        logging.error(f'Erro ao instalar o ChromeDriver: {e}')
    finally:
        logging.info('Execução finalizada')    
    


if __name__ == "__main__":
    main()
