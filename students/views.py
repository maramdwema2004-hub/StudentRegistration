from django.shortcuts import render
from .models import Student
from PIL import Image, UnidentifiedImageError

def register(request):

    error = None
    success = None

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        university_id = request.POST.get('university_id', '')
        id_number = request.POST.get('id_number', '')
        mobile_number = request.POST.get('mobile_number', '')
        address = request.POST.get('address', '').strip()
        date_of_birth = request.POST.get('date_of_birth')
        image = request.FILES.get('image')

        if not name or not all(c.isalpha() or c.isspace() for c in name):
            error = "Name must contain letters and spaces only."

        elif not university_id.isdigit() or len(university_id) != 9:
            error = "University ID must contain exactly 9 digits."

        elif university_id[0] not in ['1', '2']:
            error = "University ID must start with 1 or 2."

        elif Student.objects.filter(university_id=int(university_id)).exists():
            error = "University ID already exists."

        elif not id_number.isdigit() or len(id_number) != 9:
            error = "ID Number must contain exactly 9 digits."

        elif id_number[0] not in ['9', '8', '4']:
            error = "ID Number must start with 9, 8 or 4."

        elif not mobile_number.isdigit() or len(mobile_number) != 10:
            error = "Mobile number must contain exactly 10 digits."

        elif not mobile_number.startswith(('059', '056')):
            error = "Mobile number must start with 059 or 056."

        elif len(address) > 150:
            error = "Address must not exceed 150 characters."

        elif not date_of_birth:
            error = "Date of birth is required."

        elif not image:
            error = "Student image is required."

        elif image.name.lower().endswith(('.jpg', '.jpeg', '.png')) is False:
            error = "Image must be JPG or PNG."
        else:
            try:
                img = Image.open(image)

                if img.format not in ['JPEG', 'PNG']:
                    error = "Image must be JPG or PNG."

                else:
                    image.seek(0)

            except (UnidentifiedImageError, OSError):
                error = "Invalid image file."
        if not error:
            student = Student(
                name=name,
                university_id=int(university_id),
                id_number=int(id_number),
                mobile_number=mobile_number,
                address=address,
                date_of_birth=date_of_birth,
                image=image
            )

            student.save()
            success = "Student registered successfully!"
    return render(request, 'students/register.html',  {'error': error, 'success': success})

def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )