from algopy import ARC4Contract, String, BoxMap
from algopy.arc4 import abimethod


class FunHomework(ARC4Contract):
    def __init__(self) -> None:
        self.github_box = BoxMap(String, String)
    
    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name
    
    @abimethod()
    def set_github_handle(self, github_handle: String) -> None:
        self.github_box[String("github")] = github_handle
    
    @abimethod()
    def get_github_handle(self) -> String:
        return self.github_box[String("github")]
    
    @abimethod()
    def initialize_github_handle(self) -> None:
        self.set_github_handle(String("devblac"))
    
    @abimethod()
    def deposit(self, github_handle: String) -> String:
        """Deposit a GitHub handle into the github box"""
        self.github_box[String("github")] = github_handle
        return "Deposited GitHub handle: " + github_handle
