
import uuid   #unique session id
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from chat.models import ChatSession, ChatMessage
from chat.rag_service import get_rag_chain
# from chat.agents import run_crew_chatbot

logger = logging.getLogger(__name__)

def chat_view(request):
    return render(request, 'chat/chat.html')

# @csrf_exempt  

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            message = request.POST.get('message')
            session_id = request.POST.get('session_id') or str(uuid.uuid4())
            user = request.user if request.user.is_authenticated else None

            logger.info(f"User message: {message}")

            if user:
                session, _ = ChatSession.objects.get_or_create(session_id=session_id, user=user)
            else:
                session, _ = ChatSession.objects.get_or_create(session_id=session_id)

            ChatMessage.objects.create(session=session, message=message, is_user=True)

            qa_chain = get_rag_chain()
            result = qa_chain.invoke({"query": message})

            response = result.get("result") or result.get("answer") or str(result)

            source_docs = result.get("source_documents", [])
            for i, doc in enumerate(source_docs):
                logger.info(f"Source {i+1}: {doc.page_content[:300]}")

            # response = run_crew_chatbot(message)

            ChatMessage.objects.create(session=session, message=response, is_user=False)

            return JsonResponse({'response': response, 'session_id': session_id})

        except Exception as e:
            logger.exception("Error in chat_api")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

