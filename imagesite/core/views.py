from django.shortcuts import render, HttpResponse
from PIL import Image
import io
import base64

def home(request):
    
    return render(request, "home.html")

def compress(request):
    if request.method == "POST":
        
        file = request.FILES["user-file"]
        REDUCE_FACTOR = int(request.POST["reduce-factor"])

        filename = file.name
        original_size =  file.size / 1024

        try:
            image = Image.open(file)

            # resize the file by reducing its dimensions, i.e its len & width
            width, length = image.size
            new_width = int( (REDUCE_FACTOR / 100 ) * width )
            new_length = int( (REDUCE_FACTOR / 100 ) * length )
            image.resize((new_width, new_length), Image.LANCZOS)

            # reformat to JPEG, while reducing the image quality
            image_stream = io.BytesIO()
            image.save(image_stream, format='JPEG', quality=REDUCE_FACTOR)
            image_stream.seek(0)

            reduced_size = len(image_stream.getvalue()) / 1024

            output_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')

            return render(
                request, "compress.html",
                context={
                    "output_image": output_image,
                    "original_size": original_size,
                    "reduced_size": reduced_size,
                    "filename": filename,
                }
            )

        except Exception:
            return render(request, "home.html", context={"msg": "That file cannot be processed"})