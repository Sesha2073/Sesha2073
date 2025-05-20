import random

roasts = [
    "I'm not saying you're old, but your birth certificate is an ancient scroll.",
    "You're the reason the gene pool needs a lifeguard.",
    "If laughter is the best medicine, your face must be curing the world.",
    "You have your entire life to be a jerk. Why not take today off?",
    "I'd agree with you but then we'd both be wrong.",
    "I'm not a proctologist, but I know an asshole when I see one.",
    "If I had a face like yours, I'd sue my parents.",
    "Your family tree must be a cactus because everybody on it is a prick.",
    "Some day you'll go far. I hope you stay there.",
    "I'm jealous of people that don't know you.",
    "You're not stupid; you just have bad luck thinking.",
    "Are you always this silly, or are you making a special effort today?",
    "I've seen people like you before, but I had to pay admission.",
    "You bring everyone a lot of joy when you leave the room.",
    "I was going to give you a nasty look, but I see you already have one.",
    "If you were any less intelligent, we'd have to water you twice a week.",
    "You're the human equivalent of a participation trophy.",
    "I don't have the time or the crayons to explain this to you.",
    "Somewhere out there, a tree is tirelessly producing oxygen for you. You owe it an apology.",
    "You have a face only a mother could love, and she probably wishes she hadn't."
]

def get_name():
    name = input("Enter the name of the person you want to roast: ")
    return name

def generate_roast(name):
    joke = random.choice(roasts)
    personalized_roast = f"{name.strip()}, {joke}"
    print(personalized_roast)

if __name__ == "__main__":
    print("Welcome to the RoastMaster 3000!")
    while True:
        user_name = get_name()
        generate_roast(user_name)
        
        another = input("Want to roast someone else? (yes/no): ")
        if another.lower() != 'yes':
            break
    print("Thanks for using RoastMaster 3000! Stay frosty!")
