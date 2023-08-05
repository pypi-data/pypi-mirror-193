/************************** BEGIN cmajor-cpp-dsp.h **************************
FAUST Architecture File
Copyright (C) 2003-2022 GRAME, Centre National de Creation Musicale
---------------------------------------------------------------------
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

EXCEPTION : As a special exception, you may create a larger work
that contains this FAUST architecture section and distribute
that work under terms of your choice, so long as this FAUST
architecture section is not modified.
***************************************************************************/

#ifndef __cmajor_cpp_dsp__
#define __cmajor_cpp_dsp__

#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <algorithm>
#include <assert.h>

#include "faust/dsp/dsp.h"
#include "faust/gui/UI.h"

#include <choc/containers/choc_COM.h>
#include <choc/text/choc_JSON.h>

// Generated with 'cmaj generate --target=cpp foo.cmajor --output=cmajordsp.h'
#include "cmajordsp.h"

#define SESSION_ID 123456

/**
* Faust wrapped C++ Cmajor DSP
*/
class cmajor_cpp_dsp : public dsp {
    
    private:

        cmajordsp fDSP;
        int fSampleRate;
        choc::value::Value fControllers;
        FAUSTFLOAT* fZoneMap;
        std::map<FAUSTFLOAT*, std::function<void(FAUSTFLOAT)>> fZoneFunMap;
    
        bool startWith(const std::string& str, const std::string& prefix)
        {
            return (str.substr(0, prefix.size()) == prefix);
        }
  
        void updateControls()
        {
            for (const auto& it : fZoneFunMap) {
                it.second(*it.first);
            }
        }
    
        choc::com::String* getInputEndpoints()
        {
            return choc::com::createRawString(fDSP.inputEndpointDetailsJSON);
        }
    
    public:
    
        cmajor_cpp_dsp()
        {
            // numInputEndpoints actually counts controllers and audio inputs
            fZoneMap = new FAUSTFLOAT[fDSP.numInputEndpoints];
            fControllers = choc::json::parse(fDSP.inputEndpointDetailsJSON);
        }
    
        virtual ~cmajor_cpp_dsp()
        {
            delete [] fZoneMap;
        }
    
        virtual int getNumInputs()
        {
            return fDSP.numAudioInputChannels;
        }
    
        virtual int getNumOutputs()
        {
            return fDSP.numAudioOutputChannels;
        }
    
        virtual void buildUserInterface(UI* ui_interface)
        {
            ui_interface->openVerticalBox("CMajor");
            int i = 0;
            for (const auto& it : fControllers) {
                if (it.isObject() && it.hasObjectMember("endpointID")) {
                    std::string name = it["endpointID"].getWithDefault("");
                    uint32_t index = fDSP.getEndpointHandleForName(name);
                    if (startWith(name, "eventfCheckbox")) {
                        ui_interface->addCheckButton(name.c_str(), &fZoneMap[i]);
                        fZoneMap[i] = 0;
                        fZoneFunMap[&fZoneMap[i]] = [=](FAUSTFLOAT value) { fDSP.addEvent(index, 0, &value); };
                        i++;
                    } else if (startWith(name, "eventfButton")) {
                        ui_interface->addButton(name.c_str(), &fZoneMap[i]);
                        fZoneMap[i] = 0;
                        fZoneFunMap[&fZoneMap[i]] = [=](FAUSTFLOAT value) { fDSP.addEvent(index, 0, &value); };
                        i++;
                    } else if (startWith(name, "eventfHslider")) {
                        FAUSTFLOAT min_v = it["annotation"]["min"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT max_v = it["annotation"]["max"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT init = it["annotation"]["init"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT step = it["annotation"]["step"].getWithDefault<FAUSTFLOAT>(0);
                        ui_interface->addHorizontalSlider(name.c_str(), &fZoneMap[i], init, min_v, max_v, step);
                        fZoneMap[i] = init;
                        fZoneFunMap[&fZoneMap[i]] = [=](FAUSTFLOAT value) { fDSP.addEvent(index, 0, &value); };
                        i++;
                    } else if (startWith(name, "eventfVslider")) {
                        FAUSTFLOAT min_v = it["annotation"]["min"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT max_v = it["annotation"]["max"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT init = it["annotation"]["init"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT step = it["annotation"]["step"].getWithDefault<FAUSTFLOAT>(0);
                        ui_interface->addVerticalSlider(name.c_str(), &fZoneMap[i], init, min_v, max_v, step);
                        fZoneMap[i] = init;
                        fZoneFunMap[&fZoneMap[i]] = [=](FAUSTFLOAT value) { fDSP.addEvent(index, 0, &value); };
                        i++;
                    } else if (startWith(name, "eventfEntry")) {
                        FAUSTFLOAT min_v = it["annotation"]["min"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT max_v = it["annotation"]["max"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT init = it["annotation"]["init"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT step = it["annotation"]["step"].getWithDefault<FAUSTFLOAT>(0);
                        ui_interface->addNumEntry(name.c_str(), &fZoneMap[i], init, min_v, max_v, step);
                        fZoneMap[i] = init;
                        fZoneFunMap[&fZoneMap[i]] = [=](FAUSTFLOAT value) { fDSP.addEvent(index, 0, &value); };
                        i++;
                    } else if (startWith(name, "eventfVbargraph")) {
                        FAUSTFLOAT min_v = it["annotation"]["min"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT max_v = it["annotation"]["max"].getWithDefault<FAUSTFLOAT>(0);
                        ui_interface->addHorizontalBargraph(name.c_str(), &fZoneMap[i], min_v, max_v);
                        fZoneMap[i] = 0;
                        i++;
                    } else if (startWith(name, "eventfHbargraph")) {
                        FAUSTFLOAT min_v = it["annotation"]["min"].getWithDefault<FAUSTFLOAT>(0);
                        FAUSTFLOAT max_v = it["annotation"]["max"].getWithDefault<FAUSTFLOAT>(0);
                        ui_interface->addVerticalBargraph(name.c_str(), &fZoneMap[i], min_v, max_v);
                        fZoneMap[i] = 0;
                        i++;
                    }
                }
            }
            ui_interface->closeBox();
        }
    
        virtual int getSampleRate()
        {
            return fSampleRate;
        }
    
        virtual void init(int sample_rate)
        {
            fSampleRate = sample_rate;
            fDSP.initialise(SESSION_ID, double(sample_rate));
        }
    
        virtual void instanceInit(int sample_rate)
        {
            fSampleRate = sample_rate;
            fDSP.initialise(SESSION_ID, double(sample_rate));
        }
    
        virtual void instanceConstants(int sample_rate)
        {
            fSampleRate = sample_rate;
        }
    
        virtual void instanceResetUserInterface()
        {}
    
        virtual void instanceClear()
        {}
    
        virtual cmajor_cpp_dsp* clone()
        {
            return new cmajor_cpp_dsp();
        }
    
        virtual void metadata(Meta* m)
        {}
    
        void compute(int count, FAUSTFLOAT** inputs, FAUSTFLOAT** outputs)
        {
            // Copy audio inputs
            if (fDSP.numAudioInputChannels > 0) {
                for (int chan = 0; chan < fDSP.numAudioInputChannels; chan++) {
                    uint32_t index = fDSP.getEndpointHandleForName("input" + std::to_string(chan));
                    fDSP.setInputFrames(index, inputs[chan], count, 0);
                }
            }
           
            // Update control
            updateControls();
      
            // Render
            fDSP.advance(count);
        
            // Copy audio outputs
            if (fDSP.numAudioOutputChannels > 0) {
                for (int chan = 0; chan < fDSP.numAudioOutputChannels; chan++) {
                    int32_t index = fDSP.getEndpointHandleForName("output" + std::to_string(chan));
                    fDSP.copyOutputFrames(index, outputs[chan], count);
                }
            }
        }
    
        virtual void compute(double /*date_usec*/, int count, FAUSTFLOAT** inputs, FAUSTFLOAT** outputs)
        {
            compute(count, inputs, outputs);
        }
   
};

#endif

/************************** END cmajor-cpp-dsp.h **************************/
