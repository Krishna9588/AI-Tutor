### API Link

This API Link folder is created to display, how we can integrate Google's Gemini API into our project.

##### In this Project we are using Gemini-1.5-flash

### Modules 
- google.generativeai
  - I used this to send a request to Gemini's server.
***
  ```bash
    pip install google-generativeai
  ```
- Tkinter
  - This is used to create a pop-up window to display the answer.
  - This would not be included in our final project.
___
    
  ```bash
    pip install tk
  ```
    
#### Remember

Create your own API key from:

[Ai Studio - Google](https://aistudio.google.com/apikey)

After creating your API key go to 
[Main](main.py)
and put your API key in the place of "API Key" (inside double quotes)

#### About Main
In [Main](main.py) file
we have defined 2 main function

- get_ai_response - To handle Questions from users, Requesting Responses from the Server.
- show_popup - To display a new window for Answer
