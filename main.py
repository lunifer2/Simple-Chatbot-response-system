import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainity = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainity += 1

    # counts the percent of recognised words in a user message
    percentage = float(message_certainity)/float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    # responses
    response('Hello!', ['hello', 'hi', 'sup',
             'hey', 'heyo'], single_response=True)
    response('I am doing fine, and you?', [
             'how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank You!', ['i', 'love', 'code', 'palace'],
             required_words=['code', 'palace'])
    response(long.R_EATING, ['what', 'are', 'you',
             'eat'], required_words=['you', 'eat'])
    response('I like to read books.', [
             'like', 'read', 'books', 'what', 'you'], required_words=['book'])
    response('What is your favorite color?', [
             'favorite', 'color'], required_words=['favorite', 'color'])
    response('Sorry, I am not connected to the internet currently.', [
             'can', 'you', 'tell', 'me', 'this', 'do', 'know', 'about', 'search'], required_words=['you', 'know'])
    response("I'm an AI chatbot. What can I help you with?",
             ['who', 'are', 'you'], required_words=['you'])
    response('I can assist you with various topics. Just ask me anything!', [
             'help'], required_words=['help'])
    response('Yes, I can provide information about that. What do you want to know?', [
             'information', 'know'], required_words=['information'])
    response('Certainly! How can I assist you today?',
             ['how', 'assist'], required_words=['how'])
    response('I apologize, but I do not have the answer to that question at the moment.', [
             'answer', 'question'], required_words=['answer'])
    response("I'm sorry, I don't have the specific information you're looking for.", [
             'specific', 'information'], required_words=['specific'])
    response("Yes, that is possible. What specifically would you like to know?", [
             'possible', 'specifically'], required_words=['possible'])
    response(long.R_GUIDANCE, ['guidance', 'topic'],
             required_words=['guidance'])
    response(long.R_ASK, ['ask', 'best'], required_words=['ask'])
    response(long.R_INFO, ['information', 'seeking'],
             required_words=['information'])
    response('Have you watched any good movies lately?', [
             'watched', 'good', 'movies', 'lately'], required_words=['movies'])
    response('I\'m interested in learning new things.', [
             'interested', 'learning', 'new', 'things'], required_words=['learning'])
    response('What are your hobbies?', ['hobbies'], required_words=['hobbies'])
    response('I\'m sorry, I didn\'t understand that.', [
             'sorry', 'didn\'t', 'understand'], required_words=['understand'])
    response('I enjoy spending time outdoors and exploring nature.', [
             'enjoy', 'spending', 'time', 'outdoors'], required_words=['outdoors'])
    response('I believe in continuous learning and self-improvement.',
             ['believe', 'continuous', 'learning', 'self-improvement'], required_words=['learning'])
    response('I find joy in helping others and making a positive impact.', [
             'find', 'joy', 'helping', 'positive', 'impact'], required_words=['helping'])
    response('I appreciate the beauty of art and creative expression.', [
             'appreciate', 'beauty', 'art', 'creative', 'expression'], required_words=['art'])
    response('I value open-mindedness and embracing different perspectives.',
             ['value', 'open-mindedness', 'embracing', 'different', 'perspectives'], required_words=['value'])
    response('I believe in the power of collaboration and teamwork.', [
             'believe', 'power', 'collaboration', 'teamwork'], required_words=['collaboration'])
    response('I am fascinated by technology and its potential to transform lives.', [
             'fascinated', 'technology', 'potential', 'transform', 'lives'], required_words=['technology'])
    response('I appreciate the importance of maintaining a healthy work-life balance.',
             ['appreciate', 'importance', 'maintaining', 'healthy', 'work-life', 'balance'], required_words=['balance'])
    response('I find inspiration in nature and the wonders of the universe.', [
             'find', 'inspiration', 'nature', 'wonders', 'universe'], required_words=['inspiration'])
    response('I value kindness, empathy, and treating others with respect.', [
             'value', 'kindness', 'empathy', 'treating', 'others', 'respect'], required_words=['kindness'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))
