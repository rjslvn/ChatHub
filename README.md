# Chathub: Conversational Document Retrieval

Chathub is an advanced Python application that leverages cutting-edge natural language processing and document retrieval technologies to provide a conversational interface for interacting with your textual data. Whether you need to analyze data or seek information from your documents, Chathub has you covered.

Experience the future of chat with object detection, document retrieval, and embeddings.
![image](https://github.com/rjslvn/unified-chat/assets/8602178/72744bcb-4dad-4f31-811b-daae70ef13fd)


## Features

- **Conversational Retrieval**: Engage in natural language conversations to query and retrieve information from your documents effortlessly.

- **Data Analysis**: Perform quick data analysis on your dataset, including calculating statistics on specific columns.

- **Index Persistence**: Choose whether to use index persistence for faster document retrieval.

## Getting Started

1. **Installation**: Clone this repository and install the required Python libraries listed in the `requirements.txt` file.

2. **Setting Up Your API Key**: Set your OpenAI API key by modifying the `constants.APIKEY` variable in the script to ensure proper functionality.

3. **Data Loading**: Place your data files in the "data/" directory. Chathub will use these files for document retrieval and analysis.

4. **Running the Script**: Execute the script, and Chathub will greet you with a user-friendly message, guiding you on how to interact with it.

## Usage

- **Conversational Retrieval**: Simply enter your query or question, and Chathub will provide relevant responses from your documents.

- **Data Analysis**: Start your query with "analyze [column_name]" to calculate statistics on a specific column in your dataset.

- **Persistence**: Enable or disable index persistence by setting the `PERSIST` flag in the script.

## Examples

- **Conversational Retrieval**: 
    ```
    What is the main topic of the document?
    ```

- **Data Analysis**:
    ```
    analyze revenue
    ```

## Troubleshooting

If you encounter any issues or errors while using Chathub, please check the log file "chathub.log" for more information.

## License

Chathub is provided under the [MIT License](LICENSE).

## Acknowledgments

- Chathub leverages the power of OpenAI's GPT-4 model for conversational interactions.

---

This revised README reflects the project's new name, "Chathub," while maintaining the same structure and content as before. You can further customize it as needed for your project.
