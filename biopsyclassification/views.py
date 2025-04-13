from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .classifier import HistClassifier
import os
from django.contrib.auth.decorators import login_required

def index(request):
    """Домашняя страница."""
    return render(request, 'biopsyclassification.html')
    
@login_required
def predict(request):
    if request.method == 'POST' and request.FILES['image']:
           # Save the uploaded file to the server
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)

           # Load the trained model and make the prediction
        classifier = HistClassifier('model_weights_full.h5')
        predicted_class = classifier.classify(file_path)

        os.remove(file_path)

           # Display the predicted class to the user
        return render(request, 'result.html', {'predicted_class': predicted_class})
       
       # Render the file upload form when the request method is GET
    return render(request, 'upload.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html', {})