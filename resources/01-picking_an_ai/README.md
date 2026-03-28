# Picking an AI Subscription

To get the most out of this course, you will need access to an AI coding agent,
such as Anthropic's Claude Code or OpenAI's Codex -- in fact, some of the
assignments will *require* you to use one. Unfortunately, this means that you
*might* need to spend a little bit of money on an AI subscription. Luckily,
there are many good options available, and you can definitely get by with
spending less than $25 for the entire quarter.

Choosing an AI agent subscription can be daunting, so we will walk you through
the process below. That said, we will not require you to use any specific model
or subscription, as long as it is compatible with
[OpenCode](https://opencode.ai/) (which most are). During demos and lecture, we
will most often use OpenCode because it provides a unified interface to many
different models.

## How to decide...

Here are 3 options that together cover most people's needs:

- **Option 1: You already already have the $20/month ChatGPT Plus subscription.**
  Free (as in: no additional cost).

  If you have the $20/month ChatGPT subscription (as many of you probably do),
  then you already have access to
  [Codex](https://developers.openai.com/codex/cli), OpenAI's coding agent
  (note: free ChatGPT accounts *do not* have permanent access to Codex, but
  might have temporary access when OpenAI runs promotions -- you should check).

  The pro subscription comes with a limited amount of Codex usage, however,
  OpenAI's usage limits are quite liberal, and you should have more than enough
  for the quarter. Still, you might want to grab the free OpenAI credits for
  students at <https://developers.openai.com/community/students> just to be
  safe.

  Note that you can use your ChatGPT Plus subscription in OpenCode by following
  these [instructions](https://opencode.ai/docs/providers#openai).

- **Option 2: You don't have ChatGPT Plus, but you still want to use OpenAI's models.**
  Free.

  If you don't pay for ChatGPT Plus, and you're OK with using OpenAI's
  products, then you can redeem $100 of free Codex credits for students at
  <https://developers.openai.com/community/students>. This will allow you to
  use [Codex](https://developers.openai.com/codex/cli) for free until you run
  out of credits, which probably won't happen during the quarter (unless you go
  on a coding spree).

  Note that you can use these free OpenAI credits in
  [OpenCode](https://opencode.ai/) by following these
  [instructions](https://opencode.ai/docs/providers#openai).

- **Option 3: You don't want to use OpenAI's products.**

  If you don't want to (or can't) use OpenAI's models for any reason, we
  recommend using [OpenCode](https://opencode.ai/).

  Out of the box, OpenCode provides access to a variety of free models, such as
  *Big Pickle* and *MiniMax2.5*. These models are perhaps not as capable as
  OpenAI's models, but they should be good enough for this class. Note that
  they are *free* for an undetermined amount of time and usage -- so beware,
  they might go away during the quarter and you might need to switch to a paid
  option. Also, by using the free models, you are implicitly agreeing to let
  OpenCode collect data on your usage, which they use to improve their models
  (that's how they can afford to offer them for free).

  Beyond the free models, OpenCode also provides a cheap subscription plan
  called [OpenCode Go](https://opencode.ai/go), and a pay-as-you-go plan called
  [OpenCode Zen](https://opencode.ai/zen).

  [OpenCode Go](https://opencode.ai/go) is one of the cheapest coding agent
  subscriptions available, at $5 for the first month and then $10/month after
  that. *Go* gives you access to a handful of capable (but not quite
  best-in-class) models, like GLM-5. Usage is limited, but quite generous.

  [OpenCode Zen](https://opencode.ai/zen) is a pay-as-you-go service that
  provides access to frontier models, including the latest from OpenAI,
  Anthropic, Google and more. You pay for what you use, so it can be cheaper
  than a subscription if you don't use AI much, or more expensive if you use it
  a lot. The price also [depends](https://opencode.ai/docs/zen/#pricing) on
  which model you use. For example, as of March 2026, Qwen3 Coder is $1.50 per
  1 million output tokens, while Claude Opus 4.6 is $25. If you use Zen, we
  recommend setting monthly usage limits and making sure that auto-reload is
  disabled so that you don't accidentally rack up an unexpectedly high bill.
 
  Note that some people use both OpenCode Go and Zen at the same time -- they use
  an expensive but very capable model (like Opus) through Zen to do the
  planning, and then use a cheaper model (like GLM-5) through Go to do the
  actual implementation. This saves money while still giving good results.

## What about Claude Code?

Some of you may have heard of Claude Code and are wondering why it isn't on the
above list. In fact, Claude Code is quite good -- it's what I use -- but its
cheapest subscription (the $20/month Claude Pro plan) has quite paltry usage
limits in my experience, and so it is hard to recommend for a class where we
*want* you to use the AI a lot.

Still, Claude Code with Opus 4.6 is one of the best agentic coding experiences
available at the moment. If you want to try it out, I would recommend signing
up for the $20/month subscription with the expectation that you'll need to pair
it with one of the options above (like OpenCode Go) to get enough usage for the
quarter.

## What about local models?

There are a number of free coding agents that you can run locally, on your
own machine, at no cost (well, except for electricity). While these have the
advantage of being free, they are probably not the best choice for most
students. The reason is simple: most people do not have a machine capable of
running a capable model at any reasonable speed. For AI to be useful, it needs
to be somewhat responsive, or else you will avoid using it.

Still, if you're interested in going this route, we recommend using
[ollama](https://ollama.com/) or [LM Studio](https://lmstudio.ai/), which make
it easy to run local models. You can connect either of them to OpenCode by
following the instructions on the
[providers](https://opencode.ai/docs/providers) page of the documentation.
