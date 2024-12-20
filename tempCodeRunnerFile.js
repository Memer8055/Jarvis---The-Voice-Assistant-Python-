import OpenAI from "openai";

// OpenAI client ka instance banao
const openai = new OpenAI({
    apiKey: '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' // Yahan apna actual API key daalo
});

// Async function banao API call ke liye
async function callOpenAI() {
    try {
        const completion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo", // Model ka naam yahan sahi daalo
            messages: [
                { role: "user", content: "write a haiku about AI" }
            ]
        });

        // Response ko console mein print karo
        console.log(completion.choices[0].message.content);
    } catch (error) {
        console.error("Error occurred: ", error); // Error handle karo
    }
}

// Function ko call karo
callOpenAI();
