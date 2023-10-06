import logging.handlers

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler
LOG_FILE = '/tmp/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html>
<html>
<head>
    <title>Bio-Data</title>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #3498db;
            color: #fff;
            text-align: center;
            padding: 20px;
        }

        h1 {
            margin: 0;
        }

        .content {
            width: 80%;
            margin: 0 auto;
        }

        h2 {
            border-bottom: 2px solid #3498db;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid #ccc;
        }

        th, td {
            padding: 8px;
            text-align: left;
        }

        ul {
            list-style: none;
        }

    </style>
</head>
<body>
    <header>
        <h1>Kavya M</h1>
    </header>
    <div class="content">
            <h2>Contact</h2>
            <ul>
                <li>Email: kvmail696@gmail.com</li>
                <li>Phone: (+91) 7092772012</li>
                <li>Location: Chennai, Tamil Nadu</li>
            </ul>
       
            <h2>Experience</h2>
            <table>
                <tr>
                    <th>Position</th>
                    <th>Company</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>Data Science Intern</td>
                    <td>The Sparks Foundation</td>
                    <td>2023</td>
                </tr>
                <tr>
                    <td>Data Analyst Intern</td>
                    <td>Ozibook</td>
                    <td>2022</td>
                </tr>
            </table>

            <h2>Projects</h2>
            <ol>
                <li>PCOS Prediction using ML Algorithms</li>
                <li>Book Recommendation System</li>
		<li>Driver Vigilance Detection</li>
            </ol>

            <h2>Education</h2>
            <table>
                <tr>
                    <th>Course</th>
                    <th>College/University</th>
                    <th>Year</th>
                </tr>
                <tr>
                    <td>MSc. Data Science</td>
                    <td>Loyola college</td>
                    <td>2022-24</td>
                </tr>
                <tr>
                    <td>MSc. Mathematics</td>
                    <td>Pondicherry University</td>
                    <td>2020-22</td>
                </tr>
            </table>

            <h2>Achievements</h2>
            <ul>
                <li>Publication (in print) in Taylor and Francis book series</li>
                <li>Won first prize in project presentation at ANVAYA</li>
            </ul>

    </div>
</body>
</html>
"""


def application(environ, start_response):
    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size)
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'],
                            environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        response = ''
    else:
        response = welcome
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
