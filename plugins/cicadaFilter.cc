#include <memory>
#include <iostream>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

class CICADAFilter: public edm::global::EDFilter<>
{
    public: 
        explicit CICADAFilter(const edm::ParameterSet&);
        ~CICADAFilter() override = default;
    
    private:
        void beginJob() override{};
        bool filter(edm::StreamID, edm::Event&, edm::EventSetup const&) const override;
        void endJob() override{};

        edm::EDGetTokenT< float > anomalyToken;
        double anomalyThreshold;
};

CICADAFilter::CICADAFilter(const edm::ParameterSet& iConfig):
    anomalyToken( consumes< float > (iConfig.getParameter<edm::InputTag>("scoreSource")))
{
    anomalyThreshold = iConfig.exists("anomalyThreshold") ? iConfig.getParameter<double>("anomalyThreshold"): 0.0;
}

bool CICADAFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup& iSetup) const
{
    using namespace edm;

    edm::Handle< float > anomalyHandle;
    iEvent.getByToken(anomalyToken, anomalyHandle);

    float anomalyScore = *anomalyHandle;

    return anomalyScore > (float)anomalyThreshold;
}

DEFINE_FWK_MODULE(CICADAFilter);