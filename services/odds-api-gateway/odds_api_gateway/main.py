from app import create_rest_app, setup

if __name__ == "__main__":
    api_client = setup()
    rest_app = create_rest_app(api_client)
    rest_app.run(host="localhost", port="5000", debug=True)