import re
import logging

logging.basicConfig(filename='mexico_states_api.log', level=logging.INFO,
					format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

flask_logger = logging.getLogger(__name__)


def sanitize_string(input_string: str) -> str:
	return re.sub(r'[\\\!"\#\$%\&\'()\*,-./\:;<=>\?\@\[\]^^_`\{\|\}~+¡\ ]+', "+", input_string)


