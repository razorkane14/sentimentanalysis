# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:16:22 2025

@author: subha
"""

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download required NLTK resource
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Extracted text from the uploaded document
text = """
bhupesh!
the manager is here! get to work!
but who's that madam over there?
bharti.
learn from her.
she's the one they were talking about yesterday.
there goes your dream job.
sir.
sir you said the data operator job wasn't available.
then why did you hire that girl?
i have the same degree.
i gave the right answers in my interview.
sure. you gave the right answers.
you're qualified too. there are many factors when it comes to hiring.
sir i got 74% in b. com.
i'm very good at accounting too sir.
can you work on tally?
and excel?
i can learn it in a week sir.
bharti is there a better machineman than you on the entire floor?
you know what separates you from these men?
they're all workers. and you're a craftsman.
don't get wrapped up in all this.
soon you'll be promoted to a shift supervisor.
so i can't get the data operator job?
it's time for my morning prayer.
we'll talk about this later. now get out.
how long does it take to learn excel and tally?
three days? four days?
a week at most?
even if you learn all that you won't get the job.
what do you mean?
why can't i get the job?
say something.
is it because i don't wear makeup like her?
i have a degree too you know.
because you're bharti mandal.
do you have a privileged caste surname like banerjee or sharma?
we are dalits.
did you forget that for a moment?
they'll allow us to eat at a table but they won't let us work at one.
don't fight for what can't be yours or they'll burn you up in flames.
to hell with your fear dashrath.
please come madam. this is the canteen.
hello. priya sharma.
it's my first day at work.
would you like some stuffed okra?
where do you go when you have to pee?
where everyone goes.
but how can women go there?
do you see any women here?
you?
sit down.
miss priya you coming down here feels like... a goddess has descended upon us.
look india has progressed so much and yet there isn't a single woman in this factory.
don't look at her.
if you stare too long you'll see a beard sprouting on her face.
get back bhupesh.
she works her hands on machines all day.
she only has her hands to satisfy herself.
motherfucker.
have you gone mad? how can you hit her like that?
she threw water at me!
and you...
stop it. don't you have manners?
bharti.
ma'am stop.
no no no.
you had it coming.
take her away.
behaving like such a creep i'd say he deserves a few more slaps.
i had warned him many times.
are you okay?
yes sir.
who started the fight?
sir that long-haired man was being...
sir it's just...
let it be.
why do you do this?
it happens in every few months.
if you had hurt your hands who'd pay for the idle machines?
tell me.
be careful.
why didn't you say anything?
you are kavita.
what?
kavita was my childhood friend.
we were in high school and the holi festival was on.
as she was about to sit i kept a red water balloon on her seat.
her white skirt and panties turned totally red.
she was screaming in horror.
poor thing.
but she didn't complain just like you.
she spent all day with a sweater tied around her waist. stupid girl.
your name's bharti right?
bharti...
banerjee.
you have beautiful eyes.
i should leave now.
yeah i need to finish my joining formalities too.
i'll see you later.
believe it or not it was something like that.
the manager asked me what my hobbies were.
i told him i do palm reading.
that's it.
you learn that much in a brahmin house.
i looked at his palm and just rattled off a few things.
astrology, fortune-telling, blah blah...
and i got a call the next day.
they didn't ask you if you can work on excel and tally?
no. sir said that mr. alok will teach me everything.
everyone's so helpful.
anyway, i've managed to learn quite a bit in the last few days.
did i say something wrong?
nothing. it's just...
i miss my mom suddenly.
i can understand.
look.
neither is dashrath your best friend...
nor is kavita my friend anymore.
from today onwards we'll be friends.
okay?
i made pulao today. ma taught me.
i think i overdid the cardamom. try some?
no.
come on. just one bite.
just want to say
stay with me always
your hands these nights
our little secrets
snuck in a corner
tucked under my pillow
like a magic potion
stay with me
wherever i go
i pass through you
to find myself
just want to say
stay with me always
forever stay.
priya.
sorry i'm really late.
not at all.
and i forgot to get the box of sweets.
never mind. come in.
it smells delicious.
right?
totally.
you know i haven't had chicken since i got married.
if my in-laws find out they'll be in shock.
a sharma girl eating meat.
stop talking.
tell me how it tastes.
salt?
it's perfect.
is it salty enough?
you have magic in your hands.
give me your hands.
why?
i thought you were going to read my palm.
sorry.
i gave you sloppy kisses.
what? do you want sloppy kisses too?
come.
he just wants chicken.
i see.
so you won't share my sloppy kisses with anyone?
sorry.
no it's okay.
i understand.
come.
why did you call me here?
actually, the manager told me not to go downstairs.
he said there are strange people there and the place stinks.
please sit.
yeah.
what else?
what else did the manager say?
nothing else.
but i don't care about any of this.
you can come here.
we'll have our own small world.
our little corner.
where no men are allowed.
there are men around here.
by the way, didn't you see my whatsapp message?
yeah i did.
i won't take any excuses.
you have to come for my birthday.
shiv especially asked me to invite you.
please come?
my in-laws are after my life.
they say there are no ladies at the factory.
if they meet you they'll stop pestering me to quit.
please?
all right.
bharti. come in.
sorry.
no i'll wait outside.
come.
is she always dressed like this?
yes.
to what caste do banerjees belong?
they're bengali brahmins, ma.
be cautious about who you mingle with.
your father-in-law will be a head priest next year.
yes.
okay?
from there, yes.
from this side...
hello. how are you?
please come.
here comes the birthday girl. please come.
i'll be back in two minutes.
excuse me.
god bless you.
well, a cake contains eggs.
so my father wouldn't allow it.
he's stuck in a time warp, you see.
you're right.
so here's what i did. i worked all night churning milk and grinding nuts
and made for my beautiful wife a pristine milk cake.
here, do the honors.
keep it there.
so i shouldn't serve her?
yes, come.
it's a birthday to remember.
you deserve this first.
no, silly girl.
are you in a time warp too?
like my father.
you're getting influenced. here, eat.
why are you crying?
serve it to everyone.
we got you a birthday cake after all.
help your sister-in-law.
please have some hot samosas.
please have some.
what's the matter?
when i take a bath,
shiv irons my clothes for me.
my whatsapp reads "shiv is typing" all day.
then his messages pop up.
"what are you up to?" with a smiley.
look.
he sends me cute baby pictures every morning.
shiv wants a child
and i can't even get myself to love him.
what should i do?
is there some defect in me?
should i see a doctor?
am i crazy?
no.
it's crazy that i can't love such a nice man, right?
please.
please help me.
at times like this, i really miss kavita.
you loved kavita a lot, right?
and me?
even more than kavita.
look, there's no defect in us that needs to be fixed.
listen.
you need to own your truth.
that's the only way you can be happy.
i've accepted my truth.
now that you know a part of my truth...
another truth is that...
i'm not bharti banerjee.
my name is bharti mandal.
i'm a dalit.
my mother and granny are midwives like most women of our caste.
someone's calling.
hello, sir.
yes, sir.
sorry, sir.
yes, sir.
the manager said i've made a big blunder.
will you please come with me?
yeah, let's go.
i'm telling you the truth.
i think we are all prepared.
she's here.
you wait outside.
okay, she's here now.
happy birthday to you
happy birthday dear priya
happy birthday to you
have some snacks, sir.
before they go cold.
cut and distribute the cake to everyone.
no one's eating the samosas.
they're just sitting there.
thanks to you we've cut
a cake here for the first time.
really?
so what if you cut a cake on sunday?
your office can still celebrate on monday.
please have it.
i have an announcement to make.
i've given orders to install
a ladies' toilet in our office.
it was long overdue.
superb.
all you workers
can share the rest of the cake.
i've been looking for you everywhere.
sorry.
the manager and others were around.
or i would have fed you cake too.
you were saying something earlier, right?
about owning my truth
accepting my identity
to find happiness?
priya, i'm going to tell you something.
listen carefully.
it may sound strange at first.
you told me the other day
how kavita is so happy with her life.
think about it.
you guys had loads of fun in college.
but now she's settled in
with her new family.
she has a respectable life.
in all these years
she's never called you.
why?
because she is really happy.
she's found her identity as a mother.
similarly, the thing
that will make you feel complete…
is being a mother.
once you become a mother
you'll stop fighting within yourself.
this storm inside you will settle down.
only a child can bring you closer to shiv.
but i'm not even 25 yet.
priya, i was 18 when i had a miscarriage.
after three months my husband left me.
our palm lines often deceive us.
anyway, you're fully ready to be a mother.
you have to decide.
whether you want to suffer like me…
or live happily.
with respect.
with shiv.
think about it.
my heart's not convinced, miss bharti.
but thank you.
without your help…
i don't know what i would've done.
really.
thanks a lot.
i barely finished talking.
i just mentioned a baby
and shiv got so excited.
he was so happy
that he started making sweets at midnight.
he woke everyone up.
that's when i understood what you meant.
you were right.
i'll have a baby.
you've made the right choice.
but will you help me?
sure.
tell me. do you get your period on time?
yes.
doing it ten days before
and after the menstrual cycle
increases your chances
of getting pregnant.
the uterus opens up at this time.
wow. you know so much.
how did you learn?
the same way you learned palm reading.
right.
you'll have to keep track
of when you do it in a diary.
all right.
now i know when i'm supposed to do it…
but where?
there's no place at home.
we're a family of 12
in a two-room apartment.
no. you asked me
to feed him biscuits, right? i fed him.
shiv must be on his way.
did the manager ask about me?
yes, i told him…
"ladies' problems."
thank you. also,
i had to tally april's expense sheet…
yeah, i've done it.
it's in the expense folder.
wow!
you did it in 20 minutes flat.
it takes me at least two hours.
thank you so much.
sloppy kisses.
shiv's here.
i'll hang up now.
yeah, okay.
all the best.
thank you.
i have to leave in 15 minutes.
what?
yes.
okay, move.
sorry.
did you get hurt?
no.
forget about that.
thank you.
that's it.
are you okay?
should this be happening now?
morning sickness doesn't occur during
the last month. must be indigestion.
let's go?
are the reports okay?
yes, sir. just got
a checkup done. everything's normal.
great.
sir, you've been so helpful.
i'll be back in three months.
please don't hire someone else.
i understand.
you must take complete rest.
but we can't stall work for three months.
no, sir. that's what
i wanted to discuss with you.
bharti knows all the work.
she can manage until i'm back.
she's been helping me all these days.
all right.
i can't say no to you.
thank you, sir.
shall i leave?
sure.
three months later.
bharti. when did you come?
just now.
shut the door, please.
yes.
little prince.
looks just like you.
sit.
you look all settled.
how's everyone in the office?
everyone's fine.
what happened?
nothing.
i wonder if i made a mistake.
all day i'm either changing diapers, cooking, or breastfeeding.
and shiv seems weirdly distant lately.
he's very helpful.
but even his niceness has started to prick me.
kavita was right.
"you're married but you still want to frolic on a scooter with pompoms."
you're a mother now.
focus on your baby.
miss bharti, thank you so much.
come on.
no, really. i mean it.
she just praises you all the time.
she told us how you encouraged and supported her.
honestly, you've brought all this joy to our family.
it's nothing.
we don't want to give you more trouble.
she'll resume work this month.
right?
again?
the baby hasn't even learned how to drink milk yet
and you want her to start work?
ma.
bharti, you tell them.
priya was telling me your mother and grandma are midwives, right?
you must’ve learned such work considering the caste you belong to.
put some sense into them.
okay.
make a separate file for cash flow.
already did it, sir.
i emailed you yesterday.
i sent the purchase records too.
really?
good.
okay, sir.
by the way…
i spoke to priya.
really?
she needs some more time.
your mother's right.
it'll take you some months to regain your health.
a mother needs proper nutrition.
and looking after the baby, feeding him, changing diapers…
being a mom is a full-time responsibility.
feeding the baby, changing diapers, etc.
and then to handle office work and all that stress.
and factory conditions are so unhygienic.
it stinks so much there.
it won't be good for her health.
she seemed a bit stressed.
that would definitely affect the baby's health.
right?
she's quit the job.
so you can take over her responsibilities.
yes, sir.
as you deem fit.

"""

# Split text into sentences
sentences = text.split("\n")

# Perform sentiment analysis
sentiment_scores = [sia.polarity_scores(sentence)["compound"] for sentence in sentences if sentence.strip()]

# Categorize sentiment
positive = sum(1 for score in sentiment_scores if score > 0.05)
negative = sum(1 for score in sentiment_scores if score < -0.05)
neutral = sum(1 for score in sentiment_scores if -0.05 <= score <= 0.05)

# Plot sentiment distribution
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive, negative, neutral]
colors = ['green', 'red', 'gray']
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Sentiment Analysis Distribution")
plt.show()

# Output sentiment summary
positive, negative, neutral
