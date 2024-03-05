# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt


import logging
import azure.durable_functions as df

async def orchestrator_function(context: df.DurableOrchestrationContext):
    image_path = "image.jpg"
    
    # Call resize activity
    resized_image = await context.call_activity("resize", image_path)
    
    # Call grayscale activity using the output of resize activity
    grayscale_image = await context.call_activity("grayscale", resized_image)
    
    # Call watermark activity using the output of grayscale activity
    watermarked_image = await context.call_activity("watermark", grayscale_image)
    yield watermarked_image
main = df.Orchestrator.create(orchestrator_function)
