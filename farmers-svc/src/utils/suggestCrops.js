import { GoogleGenAI, Type } from "@google/genai";

function generateCropPrompt(
  location,
  moisture,
  nitrogen,
  phosphorus,
  potassium,
  ph,
  farmingPurpose
) {
  console.log(
    "Data: location:",
    location,
    "moisture",
    moisture,

    "nitrogen",
    nitrogen,

    "phosphorus",
    phosphorus,
    "potassium",
    potassium,
    "ph",
    ph,
    "activity",
    farmingPurpose
  );
  return `
    You are an expert agricultural advisor. Based on the given farm location, soil properties, and the farmer's reason for farming, generate a list of the most suitable crops for cultivation.
  
    Ensure the response is a structured JSON array where each crop object contains:
    - **name:** The name of the crop.
    - **suitability:** A brief explanation of why the crop is suitable for the given soil and moisture conditions.
    - **suitabilityScore:** A percentage score (0-100) indicating how well the crop matches the provided conditions.
  
    ### **Farmer's Goal:** ${
      farmingPurpose === "economic"
        ? "Maximize profit through cash crop farming."
        : "Sustain household food supply through subsistence farming."
    }
    ### **Farm Location:** ${location}
    ### **Soil Properties:**
    - **Moisture Level:** ${moisture || "moderate"}
    - **Nitrogen (N) Level:** ${nitrogen} g/kg
    - **Phosphorus (P) Level:** ${phosphorus} ppmm
    - **Potassium (K) Level:** ${potassium} ppm
    - **pH Level:** ${ph}
  
    **Guidelines:**
    - Recommend crops that align with the farmer’s goal (${farmingPurpose} farming).
    - Prioritize high-demand cash crops for economic farming.
    - Prioritize food security crops for subsistence farming.
    - Ensure the suitability description is concise yet informative.
    - Suitability scores should reflect the crop’s adaptability to the environment.
  
    **Expected JSON Response Schema:**
    [
      {
        "name": "Crop Name",
        "suitability": "Brief reason why the crop is suitable for this location and farming goal.",
        "suitabilityScore": 0-100
      }
    ]
    `;
}

export async function suggestCrop(
  location,
  moisture,
  nitrogen,
  phosphorus,
  potassium,
  ph,
  farmingPurpose = "economic"
) {
  const apiKey = process.env.GEMINI_API_KEY;

  const ai = new GoogleGenAI({ apiKey: apiKey });
  try {
    const contents = generateCropPrompt(
      location,
      moisture,
      nitrogen,
      phosphorus,
      potassium,
      ph,
      farmingPurpose
    );
    const response = await ai.models.generateContent({
      model: "gemini-2.0-flash",
      contents: contents,
      config: {
        responseMimeType: "application/json",
        responseSchema: {
          type: "array",
          items: {
            type: "object",
            properties: {
              name: {
                type: "string",
                description: "Name of the crop",
                nullable: false,
              },
              suitability: {
                type: "string",
                description:
                  "A brief explanation of why the crop is suitable for the given soil and moisture conditions.",
                nullable: false,
              },
              additions: {
                type: "string",
                description:
                  "Suggestion on what can be done to improve the productivity",
                nullable: false,
              },
              suitabilityScore: {
                type: "number",
                description:
                  "A percentage score (0-100) indicating how well the crop matches the provided conditions.",
                nullable: false,
              },
            },
            required: ["name", "suitability", "suitabilityScore", "additions"],
          },
        },
      },
    });

    if (!response || !response.text) {
      throw new Error("AI model returned an empty or invalid response.");
    }
    console.log("gemini generated suggestion");
    return JSON.parse(response.text);
  } catch (error) {
    console.error("Error generating suggestion:", error);
    if (error.message && error.message.includes("JSON")) {
      console.error("Error parsing JSON response from AI.");
    }
    if (error.message && error.message.includes("model")) {
      console.error("Error with the AI model itself.");
    }
    if (error.message && error.message.includes("network")) {
      console.error("Network error while accessing the AI model.");
    }

    throw new Error(error.message);
  }
}

// main("Mandera", 20);
