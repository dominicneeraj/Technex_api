import json

from Token.models import Word
from Token.serializers import WordSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Token.models import Word
from Token.serializers import WordSerializer
from timex import date
from Nouns import *
def formating(tok):

    fromdate = date(tok)
    if fromdate =='Any':
        Todate='Any'
    else:
       Todate='Today'

    fromperson=getFrom(tok)
    toperson=getTo(tok)
    subject = getFeature(tok, ['Subject', 'subject','as','As','about','Regarding','regarding'])
    cc=getCC(tok)
    attach=attachment(tok)
    if attach=='Any':
        HasAttachment='No'
        Attachmentname='Any'
        Attachmentsize='Any'
    elif attach in ['attachment', 'attachments']:
        HasAttachment='Yes'
        attach='Any'
        Attachmentname = attachmentname(tok)
        Attachmentsize = size(tok)

    else:
        HasAttachment='Yes'
        Attachmentname = attachmentname(tok)
        Attachmentsize = size(tok)

    data = {'From':fromperson,'To':toperson,'ToDate':Todate,'FromDate':fromdate,'HasAttachments':HasAttachment,'AttachmentType':attach,'AttachmentSize':Attachmentsize,'AttachmentName':Attachmentname,'Subject':subject,'CC':cc}
    json_data = json.dumps(data)

    response = json_data

    return response

class TokenPost(APIView):
    def post(self, request, format=None):
        print(request.data)

        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['code'] = formating(serializer.validated_data['code'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TokenList(APIView):
    """
    List all words, or create a new word.
    """
    def get(self, request, format=None):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)



class TokenDetail(APIView):
    """
    Retrieve, update or delete a word instance.
    """
    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)