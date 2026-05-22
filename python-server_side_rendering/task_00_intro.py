#!/usr/bin/python3
"""Şablon əsaslı dəvətnamə generatoru modulu."""


def generate_invitations(template, attendees):
    """Şablondakı yerləri iştirakçı məlumatları ilə doldurub fayllar yaradır."""
    # Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Boş girişlərin yoxlanılması
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər bir iştirakçının emal edilməsi
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Əvəzlənəcək açarların siyahısı
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        for placeholder in placeholders:
            # Əgər açar lüğətdə yoxdursa və ya dəyəri None-dırsa, 'N/A' qoyuruq
            val = attendee.get(placeholder)
            if val is None:
                val = "N/A"
            
            # Şablondakı {placeholder} hissəsini real dəyərlə əvəzləyirik
            target = "{" + placeholder + "}"
            processed_template = processed_template.replace(target, str(val))
        
        # Faylın adını təyin edirik: output_X.txt
        filename = f"output_{index}.txt"
        
        # Fayla yazırıq
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
