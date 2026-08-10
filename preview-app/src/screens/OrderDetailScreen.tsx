import React from 'react';
import { ArrowLeft, ChevronRight, Copy, QrCode, Phone, CheckCircle2 } from 'lucide-react';
import { Button } from '../components/ui/Button';
import { InfoCell } from '../components/ui/InfoCell';
import { StepIndicator } from '../components/ui/StepIndicator';

export function OrderDetailScreen() {
  return (
    <div className="bg-white flex flex-col w-full h-full relative overflow-y-auto overflow-x-hidden">
      {/* Top Navigation Bar */}
      <div className="flex items-center gap-4 h-12 px-4 py-3 shrink-0 w-full bg-white z-10 sticky top-0 border-b border-border-primary">
        <ArrowLeft className="w-6 h-6 text-text-primary cursor-pointer" />
        <h1 className="text-lg font-bold text-text-primary">Chi tiết đơn hàng</h1>
      </div>

      <div className="flex flex-col gap-4 p-4 pb-12 bg-gray-50">
        
        {/* Order tracking Section (Banner + Steps) */}
        <div className="flex flex-col w-full rounded-2xl bg-white shadow-sm overflow-hidden">
          {/* Banner */}
          <div className="bg-warning-secondary p-4 pr-16 relative">
            <p className="text-sm font-medium text-text-primary leading-5 relative z-10">
              Thời gian cần hoàn tất kích hoạt SIM:<br/>
              Trước 14:30 - 04/12
            </p>
            {/* Illustration placeholder */}
            <div className="absolute right-0 top-0 bottom-0 w-24 overflow-hidden pointer-events-none">
              <img src="https://i.ibb.co/VvzKqYQ/delivery-man.png" className="w-full h-full object-cover object-left opacity-90" alt="delivery" />
            </div>
          </div>
          
          <div className="p-4 flex flex-col gap-4">
            <h2 className="text-base font-bold text-text-primary">Theo dõi đơn hàng</h2>
            
            <StepIndicator 
              steps={[
                {
                  id: '1',
                  title: 'Nhận SIM',
                  status: 'completed',
                  icon: 'check'
                },
                {
                  id: '2',
                  title: 'Xác thực giấy tờ tuỳ thân',
                  description: 'Chụp ảnh giấy tờ tùy thân, ảnh chân dung',
                  status: 'current',
                  icon: 'contract',
                  action: <Button variant="solid" className="w-full">Thực hiện ngay</Button>
                },
                {
                  id: '3',
                  title: 'Ký hợp đồng',
                  status: 'pending',
                  icon: 'edit'
                },
                {
                  id: '4',
                  title: 'Gọi 900 để hoàn tất kích hoạt',
                  status: 'pending',
                  icon: 'call'
                }
              ]}
            />
          </div>
        </div>

        {/* Order Information Section */}
        <div className="bg-white border border-border-primary rounded-2xl p-4 flex flex-col gap-3 shadow-sm">
          <h2 className="text-base font-bold text-text-primary">Thông tin đơn hàng</h2>
          
          <div className="flex gap-3 items-center w-full">
            <div className="w-12 h-12 rounded-full border border-border-primary flex items-center justify-center p-1 bg-white shrink-0">
              <QrCode className="w-6 h-6 text-brand-solid" />
            </div>
            <div className="flex flex-col flex-1 gap-0.5">
              <p className="text-base font-medium text-text-primary">0842 316 555</p>
              <div className="flex items-center gap-1 text-sm text-text-primary">
                <span>Thuê bao trả trước</span>
                <span className="w-1 h-1 rounded-full bg-text-secondary"></span>
                <span>eSIM</span>
              </div>
            </div>
          </div>
          
          <Button variant="outline" className="w-full mt-1 mb-2" icon={<QrCode size={18} />}>
            Xem thông tin eSIM
          </Button>
          
          <div className="flex flex-col w-full">
            <InfoCell 
              label="Tổng thanh toán" 
              value={<span className="text-base">179.500đ</span>} 
              rightIcon={<ChevronRight size={20} className="text-text-secondary" />} 
            />
            <InfoCell 
              label="Phương thức thanh toán" 
              value={
                <div className="flex items-center gap-2">
                  <span className="bg-blue-50 text-brand-solid text-xs font-bold px-1.5 py-0.5 rounded border border-blue-200">ATM</span>
                  <span className="text-sm font-medium">*0384</span>
                </div>
              } 
            />
            <InfoCell 
              label="Mã đơn hàng" 
              value={<span className="text-sm font-medium">2512017U3P9J1G</span>} 
              rightIcon={<Copy size={16} className="text-brand-solid ml-1" />} 
            />
          </div>
          
          <div className="flex items-center justify-center pt-2">
            <button className="flex items-center justify-center gap-1 text-sm font-medium text-text-primary hover:text-brand-solid transition-colors">
              Xem chi tiết <ChevronRight size={16} />
            </button>
          </div>
        </div>

        {/* Call Support Section */}
        <div className="bg-white border border-border-primary rounded-2xl p-4 flex flex-col gap-3 shadow-sm">
          <h2 className="text-base font-bold text-text-primary">Tổng đài hỗ trợ</h2>
          <p className="text-sm text-text-primary">Để được hỗ trợ dịch vụ, bạn vui lòng liên hệ:</p>
          
          <div className="flex items-center gap-3 w-full mt-1">
            <div className="bg-brand-solid w-10 h-10 rounded-full flex items-center justify-center text-white shrink-0 shadow-sm">
              <span className="font-bold italic text-lg">V</span>
            </div>
            <div className="flex flex-col flex-1">
              <p className="text-xs text-text-secondary">Tổng đài VinaPhone</p>
              <p className="text-base font-bold text-text-primary">1800 1091</p>
            </div>
            <Button variant="icon" className="w-10 h-10 rounded-full !p-0">
              <Phone size={18} className="text-brand-solid" />
            </Button>
          </div>
        </div>

      </div>
    </div>
  );
}
