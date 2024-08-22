from flask import Flask, request, jsonify
import openai

app=Flask(__name__)

OPENAI_API_KEY="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"

openai.api_key=OPENAI_API_KEY

@app.route('/api/recognize', methods=['POST'])
def recognize_and_respond():
    try:
        data=request.json
        input_text=data.get('text')

        if not input_text:
            return jsonify({'error': 'No text provided'}),400

        response_text=generate_response(input_text)

        return jsonify({'recognized_text':input_text,'response_text':response_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

def generate_response(input_text):
    try:
        response=openai.Completion.create(
            model="text-davinci-003", 
            prompt=input_text,
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating response: {e}"

if __name__=='__main__':
    app.run(debug=True)
