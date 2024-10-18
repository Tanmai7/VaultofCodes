from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Initialize OpenAI API
openai.api_key = 'sk-b5yAcYUwoXRC6iAh4Dz1YM7fmqKV2PIkpKbZE91slMT3BlbkFJt_nACmK_czMZ1KvzUiilN0Qgo1PRSSTCLojHNbMIoA'  # Replace with your OpenAI API key

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another model of your choice
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        function_choice = request.form['function_choice']
        
        # Generate a prompt based on the user's choice
        if function_choice == 'answer':
            prompt = f"Answer this question: {user_input}"
        elif function_choice == 'summarize':
            prompt = f"Summarize the following text: {user_input}"
        elif function_choice == 'creative':
            prompt = f"Create a creative story or poem about: {user_input}"
        else:
            prompt = "Invalid function selected."

        # Get the AI's response
        ai_response = generate_response(prompt)
        return render_template('index.html', ai_response=ai_response, user_input=user_input)

    return render_template('index.html', ai_response=None)

if __name__ == '__main__':
    app.run(debug=True)
