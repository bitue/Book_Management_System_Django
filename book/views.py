from django.shortcuts import render, redirect


from book.models import Book
from .forms import BookForm


def home(request):
    return render(request, 'base.html')



def edit_book_id(request, id):
    selected_book = Book.objects.get(pk =id)
    book_form = BookForm(instance= selected_book)
    
    if request.method =='POST':
        book = BookForm(request.POST, instance=selected_book)
        if book.is_valid():
            book.save()
            return redirect('show_book')
        
    return render(request, 'store_book.html', {'form': book_form}  )


def delete_book_id(request, id):
    selected_book = Book.objects.get(pk =id).delete()
    return redirect('show_book')
    
  


def store_book(request):
    if request.POST :
        
        book = BookForm(request.POST)
        if(book.is_valid()) :
            book_instance = book.save()
            print(book.cleaned_data)
            return redirect('show_book')
        else :
            book = BookForm()
            return render(request, 'store_book.html' , {'form': book})
            
    else :
        book = BookForm(request.POST)
      
        return render(request, 'store_book.html' , {'form': book})
        

 
def show_book(request):
    books = Book.objects.all()

  
    return render(request, 'show_book.html', {'books': books } )
    
