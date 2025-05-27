class DeliveryService:
    def trackPackage(self, *args):
        if len(args) == 1:
            print(f"Tracking by package ID: {args[0]}")
        elif len(args) == 2:
            print(f"Tracking for {args[0]} on date {args[1]}")
        else:
            print("Invalid tracking input.")


dsObj = DeliveryService()
dsObj.trackPackage("PKG123")
dsObj.trackPackage("Christine Maria", "27-05-2025")
