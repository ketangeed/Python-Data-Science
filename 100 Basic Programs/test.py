import requests
import random

class JokeGenerator:
    """Generate random jokes from external APIs"""
    
    # Different joke API endpoints
    APIS = {
        'official': 'https://official-joke-api.appspot.com/random_joke',
        'jokeapi': 'https://v2.jokeapi.dev/joke/Any',
        'dad_jokes': 'https://icanhazdadjoke.com/?format=json'
    }
    
    @staticmethod
    def get_official_joke():
        """Get joke from Official Joke API"""
        try:
            response = requests.get(JokeGenerator.APIS['official'], timeout=5)
            response.raise_for_status()
            joke = response.json()
            return f"{joke['setup']}\n{joke['punchline']}"
        except Exception as e:
            return f"Error fetching joke: {e}"
    
    @staticmethod
    def get_jokeapi_joke():
        """Get joke from JokeAPI"""
        try:
            response = requests.get(JokeGenerator.APIS['jokeapi'], timeout=5)
            response.raise_for_status()
            data = response.json()
            
            if data['type'] == 'single':
                return data['joke']
            else:
                return f"{data['setup']}\n{data['delivery']}"
        except Exception as e:
            return f"Error fetching joke: {e}"
    
    @staticmethod
    def get_dad_joke():
        """Get joke from icanhazdadjoke API"""
        try:
            response = requests.get(JokeGenerator.APIS['dad_jokes'], timeout=5)
            response.raise_for_status()
            joke = response.json()
            return joke['joke']
        except Exception as e:
            return f"Error fetching joke: {e}"
    
    @classmethod
    def random_joke(cls):
        """Get a random joke from one of the APIs"""
        getter = random.choice([
            cls.get_official_joke,
            cls.get_jokeapi_joke,
            cls.get_dad_joke
        ])
        return getter()


# Usage
if __name__ == "__main__":
    generator = JokeGenerator()
    
    print("🎭 Random Joke Generator\n")
    for i in range(3):
        print(f"Joke #{i+1}:")
        print(generator.random_joke())
        print("-" * 50)