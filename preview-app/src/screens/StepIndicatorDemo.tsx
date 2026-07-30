import React from 'react';
import { OrderTrackingSection } from '../components/ui/OrderTrackingSection';
import { OrderInfoCard, SupportCard } from '../components/ui/OrderInfoSection';

export function StepIndicatorDemo() {
  return (
    <div className="w-full min-h-full bg-[#f4f6f8] relative flex flex-col items-start pb-[32px]">
        
        {/* Fake Header/Status bar space */}
        <div className="h-[44px] w-full shrink-0 bg-transparent" />
        <div className="flex gap-[16px] h-[48px] items-center px-[16px] py-[12px] w-full shrink-0 z-20 relative bg-transparent">
          <div className="w-[24px] h-[24px] shrink-0 flex items-center justify-center">
            <img src="http://localhost:3845/assets/682eda88a518e6db200fda90bc80c94a0657fec0.svg" alt="Back" className="w-full h-full" />
          </div>
          <p className="font-bold text-[18px] text-[#34404b] leading-[26px]">
            Chi tiết đơn hàng
          </p>
        </div>

        {/* Content Area */}
        <div className="flex flex-col gap-[16px] p-[16px] w-full relative z-10">
          <OrderTrackingSection />
          <OrderInfoCard />
          <SupportCard />
        </div>

    </div>
  );
}
