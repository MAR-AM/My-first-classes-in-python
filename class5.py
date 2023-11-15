class Mobile:
    def __init__(self, company_name, storage, serial_num, name, dual_sim, support_4k):
        self.company_name = company_name
        self.storage = storage
        self.serial_num = serial_num
        self.name = name
        self.dual_sim = dual_sim
        self.support_4k = support_4k

    def call(self, contact):
        print(f"{self.name} is calling {contact}.")

    def send_message(self, contact, message):
        print(f"{self.name} sent a message to {contact}: '{message}'.")

    def play_media(self, media_type):
        if self.support_4k:
            print(f"{self.name} is playing {media_type} in 4K resolution.")
        else:
            print(f"{self.name} is playing {media_type}.")

    def display_info(self):
        print(f"Company: {self.company_name}")
        print(f"Storage: {self.storage} GB")
        print(f"Serial Number: {self.serial_num}")
        print(f"Name: {self.name}")
        print(f"Dual SIM: {'Yes' if self.dual_sim else 'No'}")
        print(f"Support 4K: {'Yes' if self.support_4k else 'No'}")

# Example of using the Mobile class
mobile1 = Mobile("sumsung", 64, "SN123456", "Note 8", True, True)
mobile2 = Mobile("oppo", 128, "SN789012", "A54", False, False)
mobile3 = Mobile("Apple ",256,"SN560279", "iphon 14 pro",False,True)
# Calling methodes
mobile1.call("mother")
mobile2.send_message("Family", "Hello from my new phone :|")
mobile3.play_media("Music")

# Show mobile information
print("\nMobile 1:")
mobile1.display_info()

print("\nMobile 2:")
mobile2.display_info()

print("\nMobile 3:")
mobile3.display_info()
