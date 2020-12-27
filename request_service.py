import requests
import os


class RequestService:

    def __init__(self):
        self.__SERVER_IP = str(os.getenv("SERVER_IP"))

        self.__ADD_USER_URL = "http://" + self.__SERVER_IP + ":8080/AddNewUser"
        self.__GET_USER_URL = "http://" + self.__SERVER_IP + ":8080/GetUser"
        self.__DELETE_USER_URL = "http://" + self.__SERVER_IP + ":8080/DeleteUser"
        self.__UPDATE_USER_URL = "http://" + self.__SERVER_IP + ":8080/UpdateUser"
        self.__GET_LIST_OF_USERS_URL = "http://" + self.__SERVER_IP + ":8080/GetListOfUsers"
        self.__LOGIN_URL = "http://" + self.__SERVER_IP + ":8080/Login"

        self.__GET_LIST_OF_NOTES_URL = "http://" + self.__SERVER_IP + ":8080/GetListOfNotes"
        self.__ADD_NOTE_URL = "http://" + self.__SERVER_IP + ":8080/AddNote"
        self.__CHANGE_NOTE_URL = "http://" + self.__SERVER_IP + ":8080/ChangeNote"
        self.__DELETE_NOTE_URL = "http://" + self.__SERVER_IP + ":8080/DeleteNote"
        self.__GET_NOTE_URL = "http://" + self.__SERVER_IP + ":8080/GetNote"
        self.__GET_REPORT_URL = "http://" + self.__SERVER_IP + ":8080/GetReport"