
def handle_validation_error(error):
    print(error.messages)
    return {"message": error.messages}, 400