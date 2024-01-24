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

**Machine Learning in 2022: Embracing Uncertainty and Navigating Challenges**

As machine learning becomes increasingly integrated into our lives, it's crucial to address both its potential and pitfalls. The excitement around AI's capabilities must be tempered by concerns over our overreliance and over confidence in using these systems.

Machine learning decision-making isn't binary; it's a continuous, often volatile spectrum. This realization has led to what I see as the emergence of 'uncertainty engineering', a discipline where engineers adopt approaches akin to applied scientists, adapting to the fluid nature of AI.

In a personal project digitizing my father's collection of historical sermons using OCR, GPT-4, and DALL-E, I encountered firsthand the nuances of AI applications. The project, [Kevin-Brew.github.io](https://kevin-brew.github.io), spans documents from various eras and poses unique challenges in digitization.

**Key Insights from My Experience:**

1. **Rethinking Success Metrics**: The OCR phase highlighted the need for non-binary success metrics typically used in engineering projects. Rather than a binary 'pass/fail' approach, I found that by using applied science thinking and applying proxy metrics like the average count of dictionary words identified provided a clearly optimizable system that enabled experimentation and optimisation. The challenge for system builder is now to think about how to discover and apply metrics that track application performanve in new and novel ways.

2. **Text Cleaning with LLMs**: GPT-4's capabilities in post-processing text were impressive but not without challenges. It was able to take garbled confused text from the OCR and clean it up with beyond belief.  This process illustrated the importance of recognizing the limitations of LLMs, especially in contexts where text content abruptly changes. Here we need to relize the tasks we specific are now to a degree ambigious and yet we seek a concrete outcome. Again judicous application of data analysis and inpsection will be the new "debugging" tools of engineers in teh age of uncertainty engineering.

3. **Creativity and AI**: Using DALL-E for image generation brought to light the subjective nature of AI outputs. An image created for my wedding, initially perceived as unique, turned out to be a common output. While we have been focused on AI copying artists, if you think what you create is uinque question this.  Its very very possible and in my opinion highly likely that what you believe is now your uniquene AI creation is one of many AI-generated themes.

4. **Ethical Dilemmas**: The project also confronted ethical issues in AI, particularly around censorship and control by AI companies. I found multiple instances where GPT-4 refused to process certain content highlighted the selective approach of AI systems and the ethical implications of such controls. We need to consider, why do we allow companies like OpenAI to decide what we can generate. The censor for their own commercial interests and not for the good of mankind. When we have systems that 1/2 work how to we make sure all the content we intended to create gets out there?

**Conclusion:**

This pet project with machine learning, from OCR to text cleaning and image generation, underscores the complexity of integrating AI into practical applications. It demands a nuanced approach, considering not just the technological capabilities but also the ethical implications. As we continue to explore the possibilities of AI, let's approach its integration with a blend of critical thinking, adaptability, and ethical consideration, learning from the experiences of seasoned practitioners in the field.

