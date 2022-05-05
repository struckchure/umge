import axios from 'axios'

// axios settings

const DEBUG_MODE = process.env.NODE_ENV
let BASE_URL

switch(DEBUG_MODE) {
	case 'development':
		BASE_URL = 'http://localhost:8000'
		break;
	case 'production':
		BASE_URL = 'https://umge.herokuapp.com/'
		break;
}

axios.defaults.baseURL = BASE_URL;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.responseEncoding = 'utf8'

const api = axios.create({});

export default api
