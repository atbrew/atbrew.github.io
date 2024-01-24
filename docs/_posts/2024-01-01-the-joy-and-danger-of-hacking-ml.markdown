---
layout: post
title:  "A joys and dangers of hacking machine learning"
date:   2024-01-24 10:00:40
blurb: "The rise of uncertainty engineering"
og_image: /assets/img/content/uncertain/uncertainty_engineering_wide.png
---

<img src="{{ "/assets/img/content/uncertain/uncertainty_engineering_wide.png" | absolute_url }}" alt="Liffey swim" class="post-pic"/>
<br />
<br />

At the end of 2022 the world woke up and everyone became an expert in machine learning. This is both  exciting and scary. But I'm not scared (yet) that machines will take over the world. Im scared that I have seen humans give too much faith to machines. 

This is because we often view thing's through a binary lens, it works or it doesn't. Unfortunately when dealing with machine learning based systems the decision boundary is always continuos, even if its presented as a binary choice. What worse is the decision boundary is volitile, as we move context unexpected results emerge. 

Engineers now need to start to verse themselves in the thinking and approaches that good applied scientists have been applying for years. I believe we will start to see the emergence of a cast of engineers with a skillset of "uncertainty engineering".

I came across a few challenges in a side project I recently took on, and thought some of my relections on that project might make for a good post. I've been helping my Dad digitise his historical collection of printed sermons using OCR, GPT-4 and Dalle-3 on a github site  [kevin-brew.github.io](https://kevin-brew.github.io/).

These documents spanned from [typed text](https://kevin-brew.github.io/assets/pdf/1979-11-11-Remembrance-day-Anthony-born.pdf) (from the day I was born), to [faded laser prints](https://kevin-brew.github.io/assets/pdf/2001-09-11-Sunday-after-911.pdf) as printers changed though the years. If you want to use the [repo](https://github.com/Kevin-Brew/Kevin-Brew.github.io) for a novel dataset I'd be more than interested in seeing what you can do with it!.  

Here are some important things that resonate for me from taking this project on.

**Rethinking Success Metrics in the Age of Uncertainty, Move from Binary to Continous**

The OCR phase of the project initially followed a subjective approach, relying on a "looks good" standard. However, it soon became evident different libraries had differnt levels of output quality. [Tesseract](https://muthu.co/all-tesseract-ocr-options/) for example had a myriad of options. I played with some newer libraries and then eventuially used Google Vision.  
What I observed was my natural engineering "good enough" head coming into play. To the point I was biased towards the implementation I had made. I wasn't going to hand annotated the files, and the quality varied massively so getting a representative set would have been hard. Eventually I did a scatter plot of the number of (dictionary )words extracted from each document. This really liberated me and for an engineer we start to think less of "unit tests" and something more akin to load testing, where we make changes and try to see do we drive towards an overall optimum.     

This experience underscored the need for "uncertainty engineering" – a paradigm shift from binary success metrics to probabilistic and fuzzy metrics. By implementing a simple metric like the average count of dictionary words identified, I could better gauge the effectiveness of the OCR process, illustrating the crucial role of adaptable metrics in ML applications.

**The Double-Edged Sword of LLMs in Text Cleaning**

Building on the above, I saw that within the extracted text there were still loads of artifacts like i's that looked like l's and b's that looked like t's. I decided to use GPT-4 with the following prompt to post process the text. It was amazing, text that was barely possible the read was pulledup and out. The looks great test was working again! The challenge faced here was more nuanced. The LLM is a text generator and has a desire to "complete" generating. What I observed was some texts where the topic changed in the middle of the dicussion such as the sermon ends and then the notices are read, the LLM processing abruptly stopped. Here again, looking at the through the eyes of data fitting task helped massively. By plotting the count of "whole words" observed in the source document against the number of extracted words after LLM processing two clusters could be easily seen, documents that have been truncated and ones that handn't.   

Here we are all deligthed withm LLM's ability to translate for example, but let's consider for a moment how we inspect what's going on and make sure we get to the end? If we are running surveys how are we sure we have got there? Again here we need to consider the metrics we are tracking towards. 

**The Subjectivity of Creativity in Machine Learning**
DALL-E's role in the project was to generate images for each post, and it did so with astonishing capability. Yet, this experience brought me back to a keynote by Shai Ben-David at ECML in 2009, where he discussed the subjective nature of evaluating ML outputs, such as clustering, based on their aesthetic appeal. A personal anecdote exemplifies this: the image created for my wedding appeared unique and special but later turned out to be a common output for sermons about marriage eg. [1](https://kevin-brew.github.io/assets/img/posts/Matt%20and%20Jenni%20-%20Nov%202017.png)).

<img src="https://kevin-brew.github.io/assets/img/posts/2007-05-25-Anthony-and-Angie-Wedding-Krakow.png" alt="Two Trees Join" class="post-pic"/>

This raises critical questions about the evaluation of creativity and the assurance of uniqueness in ML-generated content. While we might see the concerns that text-to-image generators are copying artists, when we believe we are "artists" using these tools to create new things, we need to be aware that what we create is not necessarily unique. 

**The Ethical Dilemma: Censorship and Control in AI**
My biggest concern is how we are handing over censor to AI companies. They purport to be "defending" the common good, but I believe they are looking after themsleves first and foremost. I believe they  filter generation of certain images because they are concerns they will get "caught" / called out for using art-works in their training process that they had not right to.  

I also believe they act out of fear. On one hand they will claim to "defend" the common man by preventing the generation of hate speech or racy images. But who gets to decide what is tolerable? And why should that be these for profit companies?  

A core example came up in processing Dads sermons (he is definately not a fire an brimstone preecher!).I found several occasions where GPT’s refused to process specific content, like one of my father’s sermons discussing violence in Northern Ireland as it infringed on its content guidelines. This selective approach poses ethical dilemmas and raises questions about our dependency on these systems and the balance between innovation and corporate control.

**Conclusion:**
This project illuminated various challenges and considerations for engineering practitioners in the age of ML. From redefining metrics to grappling with the subjectivity of AI outputs and ethical concerns, the integration of ML in engineering requires a nuanced, informed approach. It is a journey that continues to evolve, demanding constant adaptation and critical evaluation on us as engineers.

As you progress projects that leverage these new capabilities stop and think how is this different to what we have built before. What lessons can you learn from long lived practioners in ML? Let's be deliberate about how we design systems in the age of uncertainty engineering!

