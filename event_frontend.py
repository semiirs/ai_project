import event_generator

while True:
    print("What do you want to do to Your child?")
    action = input()

    event_generator.create_event({"event_type": action})
