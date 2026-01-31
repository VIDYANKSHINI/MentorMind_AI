import { Button } from "@/components/ui/button"
import Link from "next/link"

export function Header() {
  return (
    <header className="w-full border-b border-[#37322f]/10 bg-[#f7f5f3]">
      <div className="max-w-[1060px] mx-auto px-4">
        <nav className="flex items-center justify-between py-4">
          
          {/* Brand + Nav */}
          <div className="flex items-center space-x-10">
            {/* Brand */}
            <Link href="/" className="text-[#37322f] font-semibold text-lg">
              MentorMind AI
            </Link>

            {/* Navigation */}
            <div className="hidden md:flex items-center space-x-6">
              <Link
                href="/evaluation"
                className="text-[#37322f] text-sm font-medium hover:text-[#37322f]/80 transition-colors"
              >
                Evaluation
              </Link>
              <Link
                href="/ranking"
                className="text-[#37322f] text-sm font-medium hover:text-[#37322f]/80 transition-colors"
              >
                Ranking
              </Link>
              <Link
                href="/docs"
                className="text-[#37322f] text-sm font-medium hover:text-[#37322f]/80 transition-colors"
              >
                Docs
              </Link>
            </div>
          </div>

          {/* Login */}
          <Link href="/login" aria-label="Login to MentorMind AI">
            <Button
              className="bg-[#37322f] text-white hover:bg-[#37322f]/90 focus-visible:ring-2 focus-visible:ring-[#37322f] focus-visible:ring-offset-2 transition-colors"
            >
              Login
            </Button>
          </Link>

        </nav>
      </div>
    </header>
  )
}
