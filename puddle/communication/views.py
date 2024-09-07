from django.shortcuts import render, get_object_or_404, redirect
from core.models import Item
from django.contrib.auth.decorators import login_required

from .models import Conversation
from .forms import ConversationMessageForm
# Create your views here.

@login_required
def new_conversation(request, item_pk):

    item = get_object_or_404(Item, pk = item_pk)
    # if the item is created by admin then it will be directed to dashboard

    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detailmessage',pk = conversations.first().id)# redirect to conversation with the admin and customer

    if request.method == 'POST':
        #user fill out contact form
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            #created conversation about the specific item between owner and customer
            conversation = Conversation.objects.create(item = item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)

            conversation.save()

            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()


            return redirect('item:detail', pk = item_pk)
        
    else:
        form = ConversationMessageForm()
    
    return render(request, 'communication/new.html',{
        'form' : form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request,'communication/inbox.html',{
        'conversations': conversations
    })

@login_required
def detailmessage(request,pk):
    conversation = Conversation.objects.get(members__in=[request.user.id])

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit = False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detailmessage',pk=pk)
    else: 
        form = ConversationMessageForm()

    return render(request,'communication/detailmessage.html',{
        'conversation':conversation,
        'form' : form
    })