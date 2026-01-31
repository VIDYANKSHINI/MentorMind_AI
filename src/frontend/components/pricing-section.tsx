"use client"

import { useState } from "react"

export default function EvaluationPlansSection() {
  const [billingPeriod, setBillingPeriod] = useState<"monthly" | "annually">("annually")

  const plans = {
    basic: {
      monthly: 0,
      annually: 0,
    },
    pro: {
      monthly: 15,
      annually: 12,
    },
    institutional: {
      monthly: 120,
      annually: 96,
    },
  }

  return (
    <div className="w-full flex flex-col justify-center items-center gap-2">

      {/* Header */}
      <div className="self-stretch px-6 md:px-24 py-12 md:py-16 border-b border-[rgba(55,50,47,0.12)] flex justify-center">
        <div className="max-w-[586px] text-center flex flex-col gap-4">
          <div className="text-[#49423D] text-3xl md:text-5xl font-semibold tracking-tight">
            Evaluation plans for every learner
          </div>
          <div className="text-[#605A57] text-base leading-7">
            Get AI-powered evaluations, rankings, and mentor insights.
            <br />
            Start free. Upgrade when you’re ready.
          </div>
        </div>
      </div>

      {/* Billing Toggle */}
      <div className="py-8 flex justify-center">
        <div className="flex bg-[#f0eeec] rounded-full p-1">
          <button
            onClick={() => setBillingPeriod("annually")}
            className={`px-4 py-1 rounded-full text-sm ${
              billingPeriod === "annually" ? "bg-white text-[#37322F]" : "text-[#6B7280]"
            }`}
          >
            Annually
          </button>
          <button
            onClick={() => setBillingPeriod("monthly")}
            className={`px-4 py-1 rounded-full text-sm ${
              billingPeriod === "monthly" ? "bg-white text-[#37322F]" : "text-[#6B7280]"
            }`}
          >
            Monthly
          </button>
        </div>
      </div>

      {/* Plans */}
      <div className="w-full max-w-[1060px] grid md:grid-cols-3 gap-6 py-12">

        {/* Basic */}
        <div className="border border-[#E0DEDB] p-6 flex flex-col gap-8">
          <div>
            <h3 className="text-lg font-medium text-[#37322F]">Basic</h3>
            <p className="text-sm text-[#605A57]">
              Ideal for students starting their evaluation journey.
            </p>
          </div>

          <div className="text-4xl font-semibold text-[#37322F]">
            ${plans.basic[billingPeriod]}
            <span className="text-sm font-normal"> / {billingPeriod === "monthly" ? "month" : "year"}</span>
          </div>

          <button className="bg-[#37322F] text-white rounded-full py-2 text-sm">
            Start free
          </button>

          <ul className="text-sm text-[#605A57] space-y-2">
            <li>AI-based test evaluation</li>
            <li>Basic performance reports</li>
            <li>Personal score tracking</li>
            <li>Limited ranking access</li>
          </ul>
        </div>

        {/* Pro */}
        <div className="bg-[#37322F] text-white p-6 flex flex-col gap-8">
          <div>
            <h3 className="text-lg font-medium">Pro</h3>
            <p className="text-sm text-[#D2C6BF]">
              Best for serious learners and competitive exams.
            </p>
          </div>

          <div className="text-4xl font-semibold">
            ${plans.pro[billingPeriod]}
            <span className="text-sm font-normal"> / {billingPeriod === "monthly" ? "month" : "year"}</span>
          </div>

          <button className="bg-white text-[#37322F] rounded-full py-2 text-sm">
            Get started
          </button>

          <ul className="text-sm space-y-2">
            <li>Advanced AI evaluation</li>
            <li>Detailed strengths & weaknesses</li>
            <li>National ranking & percentile</li>
            <li>Mentor recommendations</li>
            <li>Progress comparison</li>
          </ul>
        </div>

        {/* Institutional */}
        <div className="border border-[#E0DEDB] p-6 flex flex-col gap-8">
          <div>
            <h3 className="text-lg font-medium text-[#37322F]">Institutional</h3>
            <p className="text-sm text-[#605A57]">
              Designed for colleges, coaching institutes & organizations.
            </p>
          </div>

          <div className="text-4xl font-semibold text-[#37322F]">
            ${plans.institutional[billingPeriod]}
            <span className="text-sm font-normal"> / {billingPeriod === "monthly" ? "month" : "year"}</span>
          </div>

          <button className="bg-[#37322F] text-white rounded-full py-2 text-sm">
            Contact admin
          </button>

          <ul className="text-sm text-[#605A57] space-y-2">
            <li>Bulk student evaluations</li>
            <li>Institute-level analytics</li>
            <li>Custom ranking systems</li>
            <li>Admin dashboards</li>
            <li>Dedicated support</li>
          </ul>
        </div>

      </div>
    </div>
  )
}
