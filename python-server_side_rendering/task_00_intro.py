import logging
import os

# Configure logging to show error messages
logging.basicConfig(level=logging.INFO)

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    
    Returns:
        None: Creates output files or logs errors
    """
    
    # Step 1: Check input types - This is crucial for type safety
    if not isinstance(template, str):
        logging.error("Template must be a string")
        return
    
    if not isinstance(attendees, list):
        logging.error("Attendees must be a list")
        return
    
    # Step 2: Check for empty inputs - Prevents processing empty data
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return
    
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return
    
    # Step 3: Process each attendee and generate files
    for index, attendee in enumerate(attendees, 1):
        # Validate attendee is a dictionary
        if not isinstance(attendee, dict):
            logging.error(f"Attendee at index {index} is not a dictionary")
            continue
        
        # Create a copy of template for this attendee
        personalized_template = template
        
        # Replace placeholders with attendee data or "N/A" if missing
        # This handles missing data gracefully
        personalized_template = personalized_template.replace("{name}", 
            str(attendee.get("name", "N/A")))
        personalized_template = personalized_template.replace("{event_title}", 
            str(attendee.get("event_title", "N/A")))
        personalized_template = personalized_template.replace("{event_date}", 
            str(attendee.get("event_date", "N/A")))
        personalized_template = personalized_template.replace("{event_location}", 
            str(attendee.get("event_location", "N/A")))
        
        # Generate output filename
        output_filename = f"output_{index}.txt"
        
        # Step 4: Write the personalized invitation to file
        try:
            with open(output_filename, 'w') as file:
                file.write(personalized_template)
            logging.info(f"Generated {output_filename}")
        except IOError as e:
            logging.error(f"Error writing file {output_filename}: {e}")
