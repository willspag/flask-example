# flask-example
Simple Example template for a basic Flask WebApp



**Instructions**

1) Put all HTML files in frontend/html/ folder, CSS files in frontend/css/ folder, javascript files in frontend/js/ folder, and any media (pictures, etc) in the frontend/media/ folder. When linking a js/css/media file in an html file within the frontend/html/ folder, the "frontend/" folder is the root diretory, so use "frontend" should be excluded from link filepaths. For example, an HTML file, "index.html" would import:
    - A CSS file named "styles.css" using the link tag "<link href='/css/styles.css' rel='stylesheet' type='text/css' />"
    - A Javascript file named "script.js" using the script tag "<script src='/js/script.js'></script>"
    - An image file named "image.png" using the img tag "<img href='/media/image.png'>"
    - etc.

2) Build routes in the "app.py" page, and have them return pages using Flask's render_template() function with the first argument being the HTML filename of the desired webpage to return for that route (do not include the full filepath, only the file name itself - Flask is already set up to look within the "frontend/html/" folder for the file)

3) Make sure to set your environment variables. You can create a ".env" file which will automatically be loaded when "app.py" is run locally, but the ".env" file will not be included in deployment for security, so they must be set in your deployment environment (Such as a Google Cloud Run Environmental Variables). To run this code, the following environmental variables should be set
    -   FLASK_SECRET_KEY
    -   FLASK_HOST
    -   FLASK_PORT
    -   PRODUCTION_MODE_TRUE_OR_FALSE (Always set to "TRUE" when deploying your web-app)


# Deployment #
1) To use a simple python environment with pip installations:
    - Make sure that all packages used in your code (along with their version numbers) are included in the "requirements.txt" file.
    - The current Dockerfile is already set up for this deployment, so no need to change it.
    - To create a Docker Image, run "docker build -t flask-example-app ." (replace the "flask-example-app" with your new app name)
    - To Deploy the container directly to Google Cloud, run "gcloud builds submit --tag gcr.io/$GCLOUD_PROJECT_ID/flask-example-app ." (replace the "flask-example-app" with your new app name, and replace "$GCLOUD_PROJECT_ID" with your real Gcloud Project ID.

2) For more complex environments, deploy using a conda environment rather than simple pip installations.
    - Change the name of "Dockerfile" to something else (anything is fine, I would probably use "Dockerfile_pip" or something to keep everything straight)
    - Change the name of "Dockerfile_Conda" to just "Dockerfile"
    - Make sure that all of the packages used in your code exist in your current conda environment, and ensure that your conda environment is activated using "conda activate example-env" (or replace example-env with your conda environment's name). Then, export it to the "example_env.yml" file using "conda env export > example_env.yml" to overwrite the current file.
    - To create a Docker Image, run "docker build -t flask-example-app ." (replace the "flask-example-app" with your new app name)
    - To Deploy the container directly to Google Cloud, run "gcloud builds submit --tag gcr.io/$GCLOUD_PROJECT_ID/flask-example-app ." (replace the "flask-example-app" with your new app name, and replace "$GCLOUD_PROJECT_ID" with your real Gcloud Project ID.




Good luck and have fun!

