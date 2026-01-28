# Judea Pearl: The Causal Revolutionary

*The computer scientist who gave us the mathematics to say "because"*

---

In Statistics 101, every student learns to chant: "Correlation is not causation." We repeat it like a mantra. We know the rooster's crow does not cause the sunrise. We understand that ice cream sales and drowning rates both rise in summer without one causing the other.

But here is what statistics never told us: if correlation is not causation, then what *is* causation? For nearly a century, the field had no answer. The word "cause" was banished from respectable statistical discourse as unscientific, metaphysical, taboo.

Then Judea Pearl gave causation a mathematics.

## The Man Who Drew Arrows

Judea Pearl was born in Tel Aviv in 1936. He studied electrical engineering in Israel and America, worked on memory systems at RCA, and might have spent his career building better computer hardware. But in 1970, when semiconductor technology rendered his work obsolete, Pearl pivoted. He joined UCLA and began thinking about how machines might reason under uncertainty.

The first revolution came with Bayesian networks. In 1982, Pearl showed that complex probabilistic relationships could be represented as graphs---nodes connected by arrows---and that belief could propagate through these networks efficiently. The idea was simple but profound: the structure of relationships matters. A network where A causes B which causes C behaves differently than one where B causes both A and C, even if the correlations look identical.

But correlation was never Pearl's real interest. He wanted to understand cause.

## The Ladder of Causation

Pearl's central insight is that causal reasoning operates on three distinct levels, what he calls the "ladder of causation":

**Rung 1: Association (Seeing)**

At the bottom rung, we observe and correlate. We see that coffee drinkers have lower rates of depression. We note that educated people earn more. We find that hospitals have higher death rates than homes.

This is where statistics lives. This is what machine learning does. We look at data and find patterns.

But association cannot tell us *why* patterns exist. It cannot distinguish a genuine cause from a coincidence or a confound. Hospital death rates are higher because sick people go to hospitals, not because hospitals kill people. If you don't understand this distinction, you will make disastrous decisions.

**Rung 2: Intervention (Doing)**

The second rung asks a different question: what happens if we *do* something? Not "what do we observe among coffee drinkers" but "what happens if we make people drink coffee?"

This is the crucial distinction between P(Y|X)---the probability of Y given that we observed X---and P(Y|do(X))---the probability of Y if we intervene to set X.

These are different quantities. Profoundly different. And data alone cannot bridge them.

Consider: we observe that students who eat breakfast have better grades. Should we mandate breakfast programs? The association tells us nothing. Students who eat breakfast might have more stable families, more resources, more parental involvement. Breakfast might be a marker of advantage, not a cause of achievement.

To know what intervention will accomplish, we need a causal model---a diagram showing what actually causes what.

**Rung 3: Counterfactuals (Imagining)**

The highest rung asks: what *would have* happened if things had been different?

The patient died after taking the drug. Would she have died anyway? The company implemented the policy and profits rose. Did the policy cause the rise, or would it have happened regardless?

Counterfactual questions seem unanswerable---after all, we cannot observe what didn't happen. But Pearl showed that with a proper causal model, we can compute counterfactuals. We can assign probabilities to alternative histories. We can answer "why" in a mathematically rigorous way.

## The Do-Calculus

Pearl's technical contribution is a complete mathematical framework for reasoning about cause and effect.

The centerpiece is the *do*-operator. When we write do(X=x), we mean we are intervening to set X to value x---not merely observing that X happens to equal x. This simple notation captures the fundamental distinction between seeing and doing.

Pearl then developed the *do-calculus*: three rules that allow us to transform expressions involving interventions into expressions involving only observations. With these rules, plus a causal diagram representing our assumptions about what causes what, we can determine whether causal effects are identifiable from data.

The magic is in the diagram. Draw the arrows showing what causes what. From this structure, the mathematics tells you what you can conclude. Which confounders must be controlled for? What adjustment formulas apply? Can the causal effect be computed at all?

If the causal effect cannot be computed from the diagram, no amount of data will help. You need different assumptions, different data, or an experiment.

## "All the Impressive Achievements of Deep Learning Amount to Just Curve Fitting"

Pearl has been a consistent and incisive critic of modern machine learning.

His argument is simple: deep learning operates entirely on the first rung of the ladder. Neural networks learn correlations. They predict beautifully. But they cannot reason about interventions or counterfactuals because they have no causal model.

A deep learning system can learn that certain symptoms predict certain diseases. But it cannot tell you what happens if you intervene to change those symptoms. It can learn that certain applicants tend to default on loans. But it cannot tell you whether rejecting those applicants *causes* better outcomes or merely correlates with other factors.

"Deep learning has given us machines with truly impressive abilities but no intelligence," Pearl writes. "The difference is profound and lies in the absence of a model of reality."

This is not a minor limitation. Every question that matters---Should we give this drug? Should we implement this policy? Is this defendant responsible?---requires causal reasoning. Association is not enough.

## Data Are Profoundly Dumb

Perhaps Pearl's most important message is epistemological humility. Data alone cannot answer causal questions.

"Data are profoundly dumb," Pearl writes. "Data can tell you that the people who took a medicine recovered faster than those who did not take it, but they can't tell you why."

To go from correlation to causation, you need assumptions. You need to state, explicitly, what causes what. You need to draw the diagram.

This might seem like a weakness---aren't assumptions just guesses? But Pearl sees it as a strength. When your causal assumptions are explicit, they can be challenged, tested, refined. When they are hidden, they cannot be criticized, and errors propagate invisibly.

The alternative---refusing to make causal claims because we "only have observational data"---leaves us paralyzed. We cannot answer the questions that matter. We cannot understand why things happen. We cannot make good decisions.

Better to make assumptions explicit and reason carefully than to pretend we have no assumptions at all.

## The Revolutionary in Quiet Prose

Pearl writes with clarity and philosophical depth. His prose builds arguments methodically, each step justified, each distinction carefully drawn. There is no bluster, no overselling. Just the patient explanation of ideas that reshape how we think about evidence and reasoning.

He is now in his late eighties, still active, still publishing, still challenging the field. His work on causality, which began as a technical project in artificial intelligence, has transformed statistics, epidemiology, economics, and philosophy.

When Pearl received the Turing Award in 2011, the citation honored his "fundamental contributions to artificial intelligence through the development of a calculus for probabilistic and causal reasoning."

But the impact goes far beyond AI. Pearl gave us language. For centuries, humans have reasoned about cause and effect without a formal framework. We knew, intuitively, that correlation is not causation. But we could not express, mathematically, what causation *is*.

Now we can.

---

## Core Ideas for Application

**Draw the diagram first.** Before analyzing any data, sketch the causal structure. What are the variables? What causes what? The diagram is not an illustration---it is an argument.

**Classify your question.** Are you asking about association (what do I observe?), intervention (what happens if I act?), or counterfactual (what would have happened?). Each type requires different methods.

**Identify confounders.** What variables create backdoor paths between your treatment and outcome? These must be blocked---either by controlling for them statistically or by experimental design that breaks the confounding.

**Be explicit about assumptions.** Every causal conclusion rests on causal assumptions. State them. Draw them. Let them be challenged. Hidden assumptions are dangerous assumptions.

**Understand the limits of data.** More data does not climb the ladder of causation. Bigger datasets do not transform association into causation. The model---the assumed causal structure---is what allows causal conclusions.

---

*"My emphasis on language comes from a deep conviction that language shapes our thoughts. You cannot answer a question that you cannot ask, and you cannot ask a question that you have no words for."*

Pearl gave us the words for causation. Now we can ask---and answer---the questions that matter.
