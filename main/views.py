from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
# Create your views here.

form_html = """
	<form method="GET">
		<h2>Add a food</h2>
		<input type="text" name="food" value="" placeholder="What to buy?">
		%s
		<input type="submit">
	</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""

shopping_list_html = """
<br>
<br>
<h2> Shopping list</h2>
<ul>
%s
</ul>
"""

class ShoppingView(View):
	def get(self, request):
		items = range(1, 51)
		result = []

		for item in items:
			if (item%3 == 0 and item%5 == 0 and item%2 == 0):
				result.append('fizzbuzzrozz')
			elif (item%3 == 0 and item%5 == 0):
				result.append('fizzbuzz')
			elif(item%5 == 0 and item%2 == 0):
				result.append('buzzrozz')
			elif(item%3 == 0 and item%2 == 0):
				result.append('fizzrozz')
			elif (item%3 == 0):
				result.append('fizz')
			elif (item%5 == 0):
				result.append('buzz')
			elif(item%2 == 0):
				result.append('rozz')
			else:
				result.append(item)
		# result = [1,2,'fizz', 4, 'buzz']
		return HttpResponse(render(request, 'shopping_list.html', 
			{'name': request.GET.get('name'), 'items': result}))


	def post(self, request):
		return HttpResponse('Hello Post')









	# def get(self, request):
	# 	output = form_html
		
	# 	return HttpResponse(output)
